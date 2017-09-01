#!/usr/bin/python
import socket
from pymongo import MongoClient
mongo_ip = socket.gethostbyname(socket.gethostname())
client = MongoClient(mongo_ip,5000)
client.admin.authenticate('admin','admin')
db = client.workFlowDBEngine

'''
Insert the following workflow in database
'''

false = False
true = True

try:
    result = db.workflow_template.insert_one({
    "_id" : "RI_ServiceNow_Approval_AppViewX_Implement",
    "tasks" : [
        {
            "task_type" : "user",
            "task_id" : "submit",
            "roles" : [],
            "end_task" : false,
            "seq_no" : 1,
            "task_name" : "Work Order Initialization"
        },
        {
            "task_type" : "service",
            "task_id" : "aps_prevalidation",
            "roles" : [],
            "end_task" : false,
            "seq_no" : 2,
            "task_name" : "Pre Validation"
        },
        {
            "email_detail" : {
                "pre_template" : "email_awaiting_approval",
                "post_template" : "email_approved"
            },
            "roles" : [
                "admin"
            ],
            "seq_no" : 3,
            "task_name" : "Approval Level 2",
            "task_id" : "approval2",
            "task_flow" : {
                "Auto" : 5,
                "Manual" : 4
            },
            "end_task" : false,
            "tags" : {
                "action" : "implement",
                "accept_caption" : "Implement",
                "permission" : {
                    "admin" : "RW",
                    "new_user" : "R",
                    "demo_aps_role" : "R",
                    "Surya" : "R"
                }
            },
            "task_type" : "xor"
        },
        {
            "task_type" : "service",
            "task_id" : "aps_implementation",
            "roles" : [],
            "end_task" : true,
            "email_detail" : {
                "post_template" : "email_implemented"
            },
            "seq_no" : 4,
            "task_name" : "Manual Implementation"
        },
        {
            "task_type" : "timer",
            "task_id" : "ticket_validation",
            "roles" : [],
            "end_task" : false,
            "seq_no" : 5,
            "task_name" : "Ticket Validation"
        },
        {
            "task_type" : "service",
            "task_id" : "aps_implementation",
            "roles" : [],
            "end_task" : true,
            "email_detail" : {
                "post_template" : "email_implemented"
            },
            "seq_no" : 6,
            "task_name" : "Auto Implementation"
        },
        {
            "task_type" : "service",
            "task_id" : "aps_postvalidation",
            "roles" : [],
            "end_task" : true,
            "seq_no" : 7,
            "task_name" : "Post Validation"
        }
    ]
    })

    print "Successfully inserted the workflow in Data Base"
except Exception , e:
    print e