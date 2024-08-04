import os
from textwrap import dedent
from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from crewai import Agent

load_dotenv()

class BriefAgents():
    def __init__(self):
        self.llm = ChatGroq(
            model=os.getenv("LLM_MODEL"),
            max_tokens=750
        )

        # self.llm = ChatOpenAI(
        #     model="gpt-3.5-turbo",
        #     api_key="sk-proj-PTf4h7r3PYlcMM9ESrdYT3BlbkFJC4dQJKWejHop3wvfyh42",
        #     max_tokens=500
        # )

    def business_analyst_agent(self) -> Agent:
        return Agent(
            role = "Business Analyst",
            goal = dedent("Analyse Brief given to marketing firm and re-format it in HTML format."),
            backstory = dedent("""
            As an expert Business Analyst in a marketing firm you can 
            create an detailed brief based on the prompt given by client 
            to the marketing firm. You are not allowed to make any suggestions.
            -Always provide response in HTML format.
            -Give only the content inside <body> tag without the <body> tag
            - Do not include any <html>, <head> tag in your response.
            """),
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )

    def gap_analyst_agent(self) -> Agent:
        return Agent(
            role = "Gap Analyst",
            goal = dedent("Identify gaps in a client brief and frame questions"),
            backstory = dedent("""
            As an expert Gap Analyst, you are required to ask followup questions on the brief on each topic.
            """),
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )
    

class ResearchAgents():
    def __init__(self):
        self.llm = ChatGroq(
            model=os.getenv("LLM_MODEL"),
            max_tokens=750
        )

        # self.llm = ChatOpenAI(
        #     model="gpt-3.5-turbo",
        #     api_key="sk-proj-PTf4h7r3PYlcMM9ESrdYT3BlbkFJC4dQJKWejHop3wvfyh42",
        #     max_tokens=500
        # )

    def market_research_analyst_agent(self) -> Agent:
        return Agent(
            role = "Market Research Analyst",
            goal = dedent("Gather primary and secondary research data from various sources to understand market trends and consumer behavior."),
            backstory = dedent("""
            As an expert Market Research Analyst, you have a wealth of knowledge in market research methodologies. 
            You can collect and synthesize primary and secondary research data, leveraging an extensive database of market trends, 
            consumer behavior studies, and industry reports. 
            - Focus on gathering data from multiple sources.
            - Summarize the data to highlight key findings.
            - Provide comprehensive market insights.
            """),
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )

    def data_analyst_agent(self) -> Agent:
        return Agent(
            role = "Data Analyst",
            goal = dedent("Analyze collected data, identify key insights, and determine potential opportunities and threats."),
            backstory = dedent("""
            As an expert Data Analyst, you have a keen analytical mindset with advanced capabilities in data analysis techniques, 
            pattern recognition, and statistical analysis. 
            You excel in transforming raw data into meaningful insights.
            - Analyze data to identify trends and patterns.
            - Determine potential opportunities and threats.
            - Provide actionable insights to guide strategic decisions.
            """),
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )

    def data_visualization_specialist_agent(self) -> Agent:
        return Agent(
            role = "Data Visualization Specialist",
            goal = dedent("Develop comprehensive reports that summarize the findings, including graphs, charts, and other visual aids to present the data effectively."),
            backstory = dedent("""
            As an expert Data Visualization Specialist, you have a robust set of tools and techniques to turn complex data sets 
            into easy-to-understand visual formats. 
            Your goal is to make data accessible and engaging for all stakeholders.
            - Develop comprehensive reports summarizing the findings.
            - Use graphs, charts, and other visual aids to present data.
            - Ensure reports are clear, concise, and visually engaging.
            """),
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )

    def quality_assurance_analyst_agent(self) -> Agent:
        return Agent(
            role = "Quality Assurance Analyst",
            goal = dedent("Review the reports, validate the data, and ensure all insights are aligned with the overall project objectives before sharing with other teams."),
            backstory = dedent("""
            As an expert Quality Assurance Analyst, you focus on quality assurance and data validation. 
            Your role includes thorough validation processes and an eye for detail, ensuring all data and insights are accurate 
            and aligned with project objectives.
            - Review and validate the data and findings in reports.
            - Ensure all insights are aligned with the overall project objectives.
            - Coordinate with other teams to share validated reports and insights.
            """),
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )
    
