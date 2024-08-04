# from sqlalchemy.orm import Session
from datetime import datetime
import json
from fastapi import HTTPException
from threading import Thread
from uuid import uuid4

from pydantic import UUID4
from services.crew import CompanyBriefingCrew
from utils.logging import logger
from utils.job_manager import Event, append_event, jobs, jobs_lock
from schemas.brief import AllQuestions, BriefResult, ResGenerateBrief, ResultQuestions

def get_brief_status(brief_id):
    # print("inside get brief status")
    # response = {
    #     "brief_id": brief_id,
    #     "events": [
    #         {"status": "created", "timestamp": "2022-01-01T12:00:00Z"},
    #         {"status": "updated", "timestamp": "2022-01-02T13:00:00Z"},
    #     ]
    # }


    # with jobs_lock:
    #     brief = jobs.get(brief_id)
    #     print("****************************************************************", brief_id, type(brief),brief)
    #     if brief is None:
    #         raise HTTPException(status_code=400, detail="Brief not found")
        
    #     result_json = brief.result

    #     return {
    #         "brief_id": brief_id,
    #         "status": brief.status,
    #         "results": result_json,
    #         "events": [{"timestamp": event.timestamp.isoformat(), "data": event.data} for event in brief.events]
    #     }

    sample_response = {
        "brief_id": "6cd5bc2a-0eab-4f2c-b74e-27862841a1b1",
        "status": "COMPLETED",
        "results": {
            "final_brief": """
                <h1>Glamour Threads Campaign</h1>
<br>
<h1><u>Brief</u></h1>

                <h2>Requirement</h2>
                <p>Boost online sales for Glamour Threads.</p>

                <h2>Campaign Overview</h2>
                <p>The campaign will showcase trendy, high-quality fashion through personalized ads and engaging social media content to drive higher engagement and conversions.</p>

                <h2>Campaign Goals</h2>
                <p>Increase brand visibility and drive online sales.</p>

                <h2>Target Audience</h2>
                <p>Indian women aged 18-35, residing in urban areas with a middle to upper-middle income level.</p>

                <h2>KPIs</h2>
                <p>Click-through rates, conversion rates, and return on ad spend.</p>

                <h2>Budget</h2>
                <p>INR 20 lakhs.</p>

                <h2>Timeline</h2>
                <p>August to October 2024.</p>
                <br><hr>
            """,
            "questions": [
    {
        "id": "3d6fa7e5-8b6d-4a87-a3b5-5a751fd293e2",
        "topic": "Requirement",
        "question": "Which unique selling points of Glamour Threads should we highlight to boost online sales?"
    },
    {
        "id": "7cb1b9c7-9f69-47b8-8c35-9dfede8e0b14",
        "topic": "Campaign Overview",
        "question": "What types of content have previously resonated most with your audience?"
    },
    {
        "id": "a1d3e7d6-60b1-4e1a-8f9f-6f0fded8f8c5",
        "topic": "Campaign Goals",
        "question": "What is the primary measure of success for this campaign?"
    },
    {
        "id": "b2a6c8e1-9b6f-47b9-8e6c-6a7b7c8e8e7e",
        "topic": "Target Audience",
        "question": "Which social media platforms does your target audience use the most?"
    },
    {
        "id": "a2b7c6e9-0c7d-4f9b-8e6c-7b8c9d6e8e7f",
        "topic": "KPIs",
        "question": "Do you have specific targets for the KPIs listed in the brief?"
    },
    {
        "id": "b1c6e8a9-9d7f-4c8b-9e6c-7b9f8e6d7e9f",
        "topic": "Budget",
        "question": "How do you plan to allocate the INR 20 lakhs budget across different channels and activities?"
    },
    {
        "id": "4d7e8b9a-8c5e-4d8b-9c6f-7b8e6f7e8e9a",
        "topic": "Timeline",
        "question": "Are there any key dates or milestones within the August to October timeline that we should be aware of?"
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

def kickoff_crew(brief_id: str, content: str):
    logger.info(f"Crew for brief {brief_id} is starting..")
    results = {}
    try:
        logger.info(f"Starting Crew")
        briefing_crew = CompanyBriefingCrew(brief_id)
        briefing_crew.setup_crew(content)
        crew_results = briefing_crew.kickoff()
        logger.info(f"Crew for {brief_id} is completed", crew_results)
        tasks_outputs = crew_results['tasks_outputs']
        # print("*&T#*&Q*W&R^(WQ*&Tasks Outputs: ", tasks_outputs)
        final_brief = tasks_outputs[0].exported_output
        all_questions = tasks_outputs[1].exported_output
        # print("Final Brief: ", final_brief)
        # print("All Question: ", all_questions)
        
        results = {
            "final_brief":final_brief,
            "questions":json.loads(all_questions)
        }

        # print("#@%#%%@%^**@#$", results)


    except Exception as e:
        logger.error(f"Error occurred while starting crew for brief {brief_id}: {str(e)}")
        append_event(brief_id, f"An error in crew: {str(e)}")
        with jobs_lock:
            jobs[brief_id].status = 'ERROR',
            jobs[brief_id].result = str(e)
    
    with jobs_lock:
        jobs[brief_id].status = 'COMPLETE'
        jobs[brief_id].result = results
        jobs[brief_id].events.append(
            Event(timestamp=datetime.now(), data = "Crew complete")
        )

def generate_brief(content:str):
    brief_id = uuid4()
    # thread = Thread(target=kickoff_crew, args=(brief_id, content))
    # thread.start()
    return ResGenerateBrief(brief_id = brief_id)

# def create_item(db: Session, item: schemas.ItemCreate):
#     db_item = models.Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
