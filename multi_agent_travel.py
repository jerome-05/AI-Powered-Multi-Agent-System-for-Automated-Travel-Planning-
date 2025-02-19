from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEndpoint
import os
import logging
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load API keys securely from environment variables
os.environ["SERPAPI_API_KEY"] = "60a291827fc073ecfeec0d25a7a5a81071c19518320a970538918bb3ad4daaf3"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize Hugging Face LLM
llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct",
    task="text-generation",
    temperature=0.7,
    model_kwargs={"max_length": 512}
)

# Initialize SERP API Wrapper
search = SerpAPIWrapper()

# --- Function Definitions ---
def flight_search(origin: str, destination: str, departure_date: str, return_origin: str = None, return_destination: str = None, return_date: str = None):
    """Searches for one-way or round-trip flights using the SerpAPI."""
    departure_query = f"flights from {origin} to {destination} on {departure_date}"
    logger.info(f"Searching for flights: {departure_query}")
    departure_result = search.run(departure_query)

    flight_data = {
        "departure": {
            "origin": origin,
            "destination": destination,
            "date": departure_date,
            "flights": departure_result  # Replace with parsed flight data
        }
    }

    # If return details are provided, search for return flights
    if return_origin and return_destination and return_date:
        return_query = f"flights from {return_origin} to {return_destination} on {return_date}"
        logger.info(f"Searching for return flights: {return_query}")
        return_result = search.run(return_query)
        flight_data["return"] = {
            "origin": return_origin,
            "destination": return_destination,
            "date": return_date,
            "flights": return_result  # Replace with parsed return flight data
        }

    return json.dumps(flight_data)

def hotel_search(destination: str, checkin_date: str, checkout_date: str):
    """Searches for hotels using the SerpAPI and returns structured data."""
    query = f"hotels in {destination} from {checkin_date} to {checkout_date}"
    logger.info(f"Searching for hotels: {query}")
    result = search.run(query)
    return json.dumps({
        "destination": destination,
        "checkin_date": checkin_date,
        "checkout_date": checkout_date,
        "hotels": result  # Replace with parsed hotel data
    })

def itinerary_plan(destination: str):
    """Plans an itinerary using the SerpAPI and returns structured data."""
    query = f"top attractions in {destination}"
    logger.info(f"Planning itinerary: {query}")
    result = search.run(query)
    return json.dumps({
        "destination": destination,
        "attractions": result  # Replace with parsed itinerary data
    })

def budget_management(flight_cost: float, hotel_cost: float, activities_cost: float, total_budget: float):
    """Calculates the remaining budget."""
    remaining_budget = total_budget - (flight_cost + hotel_cost + activities_cost)
    logger.info(f"Calculating budget: Remaining ${remaining_budget:.2f}")
    return f"Remaining budget: ${remaining_budget:.2f}"

# --- Tool Setup ---
flight_tool = Tool(
    name="Flight Finder",
    func=lambda input_text: flight_search(*input_text.split(", ")),
    description="Finds flights based on origin, destination, and dates. Input format: 'origin, destination, departure_date, return_origin, return_destination, return_date' (for round-trip) or 'origin, destination, departure_date' (for one-way)."
)

hotel_tool = Tool(
    name="Hotel Finder",
    func=lambda input_text: hotel_search(*input_text.split(", ")),
    description="Finds hotels in a given location and date range. Input format: 'destination, check-in-date, check-out-date'"
)

itinerary_tool = Tool(
    name="Itinerary Planner",
    func=lambda destination: itinerary_plan(destination.strip()),
    description="Generates an itinerary for a trip based on the destination."
)

budget_tool = Tool(
    name="Budget Manager",
    func=lambda input_text: budget_management(*[float(x.strip("'")) for x in input_text.split(", ")]),
    description="Tracks expenses and remaining budget. Input format: 'flight_cost, hotel_cost, activities_cost, total_budget'"
)

# Initialize Conversation Memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize Agent
agent = initialize_agent(
    tools=[flight_tool, hotel_tool, itinerary_tool, budget_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
    max_iterations=10,  # Increased iteration limit
    handle_parsing_errors=True
)

# --- Example Execution ---
def run_agent(input_text: str):
    """Runs the agent with the given input and logs the response."""
    logger.info(f"Running agent with input: {input_text}")
    try:
        response = agent.invoke({"input": input_text})
        logger.info(f"Agent Response: {response}")

        # Extract and format the output for better readability
        output = response.get("output", "No output generated.")
        chat_history = response.get("chat_history", [])

        # Print the final output in a human-readable format
        print("\n--- Final Output ---")
        print(output)

        # Optionally, print the chat history for debugging
        print("\n--- Chat History ---")
        for message in chat_history:
            print(f"{message.type.capitalize()}: {message.content}")

        return response
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        return {"error": str(e)}

# Test the agent
if __name__ == "__main__":
    input_text = "I want to fly from New York to Paris on March 20th and return on March 27th. My budget is $2000. Find me flights, hotels, and an itinerary."
    response = run_agent(input_text)
    print(response)