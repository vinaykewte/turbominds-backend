from uuid import uuid4
from schemas.research import ResGenerateResearch

def generate_research(data):
    research_id = uuid4()
    print(data)
    # thread = Thread(target=kickoff_crew, args=(brief_id, content))
    # thread.start()
    return ResGenerateResearch(research_id = research_id)

def get_research_status(research_id):
    # print("getting research status...", research_id)
    sample_response = {
        "research_id": research_id,
        "status": "COMPLETED",
        "results": {
            "final_research": """
                <h1><u>Research</u></h1>


                <h2>Buying Patterns</h2>

                <h2>1. Preference for Online Shopping</h2>
                <p>Urban Indian women aged 18-35 are increasingly turning to online shopping, with 70% of this demographic preferring to shop online due to convenience and the availability of a wider range of products.</p>

                <h2>2. Influence of Social Media</h2>
                <p>Approximately 80% of young women in India are influenced by social media when making purchasing decisions. Platforms like Instagram and Facebook play a crucial role in shaping their fashion choices, with 60% following fashion influencers for style inspiration.</p>

                <h2>3. Brand Loyalty and Quality</h2>
                <p>Around 65% of consumers in this age group express brand loyalty, often preferring brands that offer high-quality, trendy products. Quality and style are significant factors, with 75% willing to pay a premium for products that meet their expectations.</p>

                <h2>4. Seasonal and Festive Buying Trends</h2>
                <p>Buying patterns also shift during festive seasons, with a reported increase of 50% in online fashion purchases during major festivals. This trend highlights the importance of aligning marketing campaigns with cultural events.</p>

                <h2>5. Sustainability Concerns</h2>
                <p>A growing number of consumers (about 55%) are considering sustainability in their purchasing decisions. Brands that promote eco-friendly practices and materials are likely to attract this environmentally conscious demographic.</p>

                <h2>Sources</h2>

                <ul>
                    <li><a href="https://soravjain.com/social-media-marketing-campaigns-india/">Social Media Marketing Campaigns in India</a></li>
                    <li><a href="https://www.campaignindia.in/article/threads-a-brand-engagement-powerhouse-or-a-fad/490957">Threads: A Brand Engagement Powerhouse or a Fad?</a></li>
                    <li><a href="https://www.thevoiceoffashion.com/fabric-of-india/features/breaking-good-with-raw-mangos-brand-campaigns-4590">Breaking Good with Raw Mango's Brand Campaigns</a></li>
                    <li><a href="https://www.grynow.in/blog/top-indian-fashion-influencers.html">Top Fashion Influencers in India</a></li>
                    <li><a href="https://www.thevoiceoffashion.com/intersections/culture/festive-campaigns-that-charm-and-churn-5246">Festive Campaigns That Charm and Churn</a></li>
                </ul><hr>
                """,
            "sources": [
                {
                    "id": "d4d1b0a8-bc30-4f3b-b8b7-ccf57c5b8d4c",
                    "url": "https://soravjain.com/social-media-marketing-campaigns-india/",
                    "title": "Social Media Marketing Campaigns in India"
                },
                {
                    "id": "7e5c8c7b-0f71-4d5a-9d5b-1c9cf4f1c43a",
                    "url": "https://www.campaignindia.in/article/threads-a-brand-engagement-powerhouse-or-a-fad/490957",
                    "title": "Threads: A Brand Engagement Powerhouse or a Fad?"
                },
                {
                    "id": "4b8d6742-d62c-4ae8-934b-865f8f2e78db",
                    "url": "https://www.thevoiceoffashion.com/fabric-of-india/features/breaking-good-with-raw-mangos-brand-campaigns-4590",
                    "title": "Breaking Good with Raw Mango's Brand Campaigns"
                },
                {
                    "id": "99f4a1c5-d24a-4d76-b51c-94ebcd1de80e",
                    "url": "https://www.grynow.in/blog/top-indian-fashion-influencers.html",
                    "title": "Top Fashion Influencers in India"
                },
                {
                    "id": "99e4e6f0-7dc4-4a1f-8c65-9457bfc8e48e",
                    "url": "https://www.thevoiceoffashion.com/intersections/culture/festive-campaigns-that-charm-and-churn-5246",
                    "title": "Festive Campaigns That Charm and Churn"
                }
            ]

        },
        "events": [
            {
            "timestamp": "2024-07-18T16:57:20.655339",
            "data": "Task Started"
            },
            {
            "timestamp": "2024-07-18T16:57:24.867423",
            "data": "Agent 1 Completed"
            },
            {
            "timestamp": "2024-07-18T16:57:34.090442",
            "data": "Agent 2 Completed"
            },
            {
            "timestamp": "2024-07-18T16:57:34.090880",
            "data": "Task Completed"
            },
            {
            "timestamp": "2024-07-18T16:57:34.090930",
            "data": "Crew complete"
            }
        ]
        }
            
    return sample_response