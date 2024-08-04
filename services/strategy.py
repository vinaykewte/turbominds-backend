from uuid import uuid4
from schemas.strategy import ResGenerateStrategy

def generate_strategy(data):
    strategy_id = uuid4()
    print(data)
    # thread = Thread(target=kickoff_crew, args=(brief_id, content))
    # thread.start()
    return ResGenerateStrategy(strategy_id = strategy_id)

def get_strategy_status(strategy_id):
    # print("getting research status...", research_id)
    sample_response = {
        "strategy_id": strategy_id,
        "status": "COMPLETED",
        "results": {
            "final_strategy": """
                   <h1><u>Strategy</u></h1>

    <h2>Platform Strategy</h2>
    <h3>1. Instagram</h3>
    <p>Utilize Instagram for its visual appeal and high engagement rates. Post high-quality images and short videos of the latest collections, run targeted ads, and collaborate with influencers for sponsored posts and stories.</p>
    
    <h3>2. Facebook</h3>
    <p>Leverage Facebook’s broad reach to engage with users through both organic posts and paid advertisements. Create events and promotions, and use Facebook Ads to target specific demographics with tailored messaging.</p>
    
    <h3>3. Twitter</h3>
    <p>Use Twitter for real-time engagement and updates. Share fashion tips, respond to customer inquiries, and participate in trending conversations to boost brand visibility.</p>
    
    <h3>4. Pinterest</h3>
    <p>Create visually appealing pins and boards showcasing fashion collections, style guides, and seasonal trends. Pinterest is ideal for driving traffic to the website and enhancing brand awareness through visual content.</p>
    
    <h3>5. YouTube</h3>
    <p>Produce and share video content, such as fashion lookbooks, behind-the-scenes footage, and influencer collaborations. Use YouTube Ads to reach a broader audience and drive traffic to the brand’s website.</p>

    <h2>Content Strategy</h2>
    <p>Develop a mix of content types tailored to each platform’s strengths. Focus on high-quality visuals, engaging videos, and informative posts that highlight the brand's unique selling points and resonate with the target audience.</p>

    <h2>Creative Assets Needed</h2>
    <ul>
        <li>High-resolution images of fashion collections</li>
        <li>Short-form videos and reels for social media</li>
        <li>Infographics showcasing style tips and trends</li>
        <li>Branded templates for posts and stories</li>
        <li>Ad creatives for targeted campaigns</li>
        <li>Influencer collaboration content</li>
    </ul>

    <h2>Content Mix</h2>
    <ul>
        <li>Product showcases (40%)</li>
        <li>Influencer content (20%)</li>
        <li>Behind-the-scenes (15%)</li>
        <li>Style guides and tips (15%)</li>
        <li>Festive and seasonal promotions (10%)</li>
    </ul>

    <h2>Posting Schedule with Frequency</h2>
    <ul>
        <li>Instagram: 4-5 posts per week, daily stories</li>
        <li>Facebook: 3-4 posts per week, bi-weekly ads</li>
        <li>Twitter: 5-6 tweets per week, daily interactions</li>
        <li>Pinterest: 3-4 pins per week</li>
        <li>YouTube: 1 video per week</li>
    </ul>

    <h2>Strategies</h2>
    <ul>
        <li>Leverage influencers to create authentic content and broaden reach.</li>
        <li>Run targeted ads during peak hours and festive seasons for maximum impact.</li>
        <li>Engage with followers through interactive content like polls and Q&As.</li>
        <li>Align content with seasonal trends and cultural events for increased relevance.</li>
        <li>Monitor trends and adapt strategies based on real-time data and feedback.</li>
    </ul>

    <h2>Popular Hashtags and Discoverability</h2>
    <p>Use relevant and trending hashtags to enhance discoverability:</p>
    <ul>
        <li>#FashionTrends</li>
        <li>#StyleInspiration</li>
        <li>#OOTD (Outfit Of The Day)</li>
        <li>#FashionGoals</li>
        <li>#TrendyLooks</li>
        <li>#GlamourThreads</li>
        <li>#FestiveFashion</li>
    </ul>

    <h2>Targeted SEO Keywords</h2>
    <ul>
        <li>Trendy fashion for women</li>
        <li>High-quality fashion online</li>
        <li>Latest fashion trends India</li>
        <li>Stylish outfits for women</li>
        <li>Eco-friendly fashion brands</li>
        <li>Urban fashion for women</li>
    </ul>

    <h2>Performance Metrics</h2>
    <ul>
        <li>Reach and impressions</li>
        <li>Engagement rates (likes, comments, shares)</li>
        <li>Website traffic and referral sources</li>
        <li>Growth in social media followers</li>
        <li>Influencer engagement and effectiveness</li>
    </ul>

    <h2>KPIs</h2>
    <ul>
        <li>Increase in brand awareness by 30%</li>
        <li>Achieve a 15% growth in social media followers</li>
        <li>Drive 20% more traffic to the website</li>
        <li>Enhance engagement rates by 25%</li>
        <li>Generate a 10% increase in brand mentions across social media platforms</li>
    </ul>
            """
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