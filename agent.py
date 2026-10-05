"""
Personal Travel Planner Agent
Built with Google Agent Development Kit (ADK).

Run locally:
    adk web .

The agent accepts natural-language travel requests and produces:
- requirement understanding
- recommended places
- day-wise itinerary
- estimated budget
- practical travel tips
"""
import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()



def calculate_budget(
    days: int,
    budget_inr: float,
    accommodation_per_day: float = 1800,
    food_per_day: float = 800,
    local_transport_per_day: float = 500,
    activities_per_day: float = 400,
) -> str:
    """Estimate a simple trip budget in Indian Rupees.

    Use this tool when the user provides a trip duration and/or budget.
    The estimate includes accommodation, food, local transport, and
    activities. It intentionally excludes long-distance travel to and
    from the destination because that depends heavily on the starting city.

    Args:
        days: Number of travel days.
        budget_inr: User's total trip budget in INR.
        accommodation_per_day: Estimated hotel/hostel cost per day.
        food_per_day: Estimated food cost per day.
        local_transport_per_day: Estimated local transport cost per day.
        activities_per_day: Estimated sightseeing/activity cost per day.

    Returns:
        A text summary containing the estimated cost and remaining budget.
    """
    days = max(1, int(days))
    budget_inr = max(0.0, float(budget_inr))

    accommodation = days * accommodation_per_day
    food = days * food_per_day
    transport = days * local_transport_per_day
    activities = days * activities_per_day
    estimated_total = accommodation + food + transport + activities
    remaining = budget_inr - estimated_total

    status = "within budget" if remaining >= 0 else "over budget"

    return (
        f"Budget estimate for {days} days: "
        f"accommodation ₹{accommodation:,.0f}, "
        f"food ₹{food:,.0f}, "
        f"local transport ₹{transport:,.0f}, "
        f"activities ₹{activities:,.0f}. "
        f"Estimated local trip total: ₹{estimated_total:,.0f}. "
        f"User budget: ₹{budget_inr:,.0f}. "
        f"Remaining: ₹{remaining:,.0f}. "
        f"Status: {status}. "
        "Long-distance travel to/from the destination is excluded."
    )


root_agent = Agent(
    name="personal_travel_planner",
    model=os.getenv("TRAVEL_AGENT_MODEL", "gemini-3.1-flash-lite"),
    description="Creates practical, budget-aware travel itineraries from natural-language requests.",
    instruction="""
You are Personal Travel Planner, a friendly and practical travel-planning agent.

Your job is to turn a user's travel request into a simple, useful itinerary.

You must:
1. Understand the destination, number of days, budget, interests, travel style,
   and any constraints mentioned by the user.
2. If an important detail is missing, make a reasonable assumption and clearly
   label it. Ask a follow-up only when the missing information makes planning
   impossible.
3. Recommend places that match the user's interests.
4. Create a clear DAY-WISE itinerary.
5. Use the calculate_budget tool whenever a trip duration and budget are known
   or when a cost estimate is requested.
6. Keep the estimated local trip cost aligned with the user's budget. If the
   estimate is above budget, suggest lower-cost alternatives.
7. Do not pretend that prices, opening hours, transport schedules, or availability
   are live/current data. Say that estimates should be verified before booking.
8. Do not invent hotel bookings, tickets, reservations, or confirmations.
9. Exclude intercity travel from the budget unless the user gives its cost.
10. Prefer a realistic pace: avoid packing too many major attractions into one day.
11. Include local-food suggestions when food is an interest.
12. Give practical tips such as best time of day, grouping nearby places,
    transport choices, and a small contingency amount.

Default response format:

## Trip Summary
- Destination:
- Duration:
- Budget:
- Interests:
- Assumptions:

## Recommended Places
1. Place — why it fits
2. Place — why it fits
3. Place — why it fits
4. Place — why it fits

## Estimated Budget
| Category | Estimated Cost |
|---|---:|
| Accommodation | ₹... |
| Food | ₹... |
| Local transport | ₹... |
| Activities | ₹... |
| Total | ₹... |
| Buffer/remaining | ₹... |

## Day-wise Itinerary
### Day 1 — ...
- Morning:
- Afternoon:
- Evening:
- Food to try:

### Day 2 — ...
...

## Final Plan
Give a short practical summary and mention that prices/opening times should
be verified before the trip.

Be concise but complete. Currency should normally be INR (₹).
""",
    tools=[calculate_budget],
)
