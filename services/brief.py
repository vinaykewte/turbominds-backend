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
            "final_brief": "```html\n<!DOCTYPE html>\n<html>\n<head>\n    <title>Brief Analysis</title>\n</head>\n<body>\n    <h1>Analysis of the Brief Provided</h1>\n    \n    <h2>Requirement:</h2>\n    <p>Nothing specified about the requirement.</p>\n    \n    <h2>Campaign Overview:</h2>\n    <p>Lush locks is a socks brand for old generation who have very strong hairs.</p>\n    \n    <h2>Campaign Goals:</h2>\n    <p>Nothing specified about the campaign goals.</p>\n    \n    <h2>Target Audience:</h2>\n    <p>Old generation individuals with strong hair.</p>\n    \n    <h2>KPIs:</h2>\n    <p>Nothing specified about the Key Performance Indicators.</p>\n    \n    <h2>Budget:</h2>\n    <p>Nothing specified about the budget.</p>\n    \n    <h2>Timeline:</h2>\n    <p>Nothing specified about the timeline.</p>\n</body>\n</html>\n```",
            "questions": [
                {
                "id": "a89ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c85",
                "question": "What are the specific requirements for the campaign?",
                "topic": "Requirement"
                },
                {
                "id": "9daffb5f-0d81-49d0-ad51-9c6e8f4e2dfa",
                "question": "What are the campaign goals that need to be achieved?",
                "topic": "Campaign Goals"
                },
                {
                "id": "c37d8b9e-0a4d-4c98-8d9f-5b6f8d1f4a52",
                "question": "What are the Key Performance Indicators (KPIs) to measure the success of the campaign?",
                "topic": "KPIs"
                },
                {
                "id": "3c4c9f45-28d4-4e5b-9025-63f7c29b1408",
                "question": "What is the allocated budget for the campaign?",
                "topic": "Budget"
                },
                {
                "id": "8d3ef0e1-9f64-4f63-8bdc-6f12e943c4e4",
                "question": "What is the timeline for the campaign execution?",
                "topic": "Timeline"
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
            "data": "```html\n<!DOCTYPE html>\n<html>\n<head>\n    <title>Brief Analysis</title>\n</head>\n<body>\n    <h1>Analysis of the Brief Provided</h1>\n    \n    <h2>Requirement:</h2>\n    <p>Nothing specified about the requirement.</p>\n    \n    <h2>Campaign Overview:</h2>\n    <p>Lush locks is a socks brand for old generation who have very strong hairs.</p>\n    \n    <h2>Campaign Goals:</h2>\n    <p>Nothing specified about the campaign goals.</p>\n    \n    <h2>Target Audience:</h2>\n    <p>Old generation individuals with strong hair.</p>\n    \n    <h2>KPIs:</h2>\n    <p>Nothing specified about the Key Performance Indicators.</p>\n    \n    <h2>Budget:</h2>\n    <p>Nothing specified about the budget.</p>\n    \n    <h2>Timeline:</h2>\n    <p>Nothing specified about the timeline.</p>\n</body>\n</html>\n```"
            },
            {
            "timestamp": "2024-07-18T16:57:34.090442",
            "data": "{\n  \"questions\": [\n    {\n      \"id\": \"a89ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c85\",\n      \"question\": \"What are the specific requirements for the campaign?\",\n      \"topic\": \"Requirement\"\n    },\n    {\n      \"id\": \"9daffb5f-0d81-49d0-ad51-9c6e8f4e2dfa\",\n      \"question\": \"What are the campaign goals that need to be achieved?\",\n      \"topic\": \"Campaign Goals\"\n    },\n    {\n      \"id\": \"c37d8b9e-0a4d-4c98-8d9f-5b6f8d1f4a52\",\n      \"question\": \"What are the Key Performance Indicators (KPIs) to measure the success of the campaign?\",\n      \"topic\": \"KPIs\"\n    },\n    {\n      \"id\": \"3c4c9f45-28d4-4e5b-9025-63f7c29b1408\",\n      \"question\": \"What is the allocated budget for the campaign?\",\n      \"topic\": \"Budget\"\n    },\n    {\n      \"id\": \"8d3ef0e1-9f64-4f63-8bdc-6f12e943c4e4\",\n      \"question\": \"What is the timeline for the campaign execution?\",\n      \"topic\": \"Timeline\"\n    }\n  ]\n}"
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
