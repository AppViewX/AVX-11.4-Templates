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
    "_id" : "ADC_Prov_implement_Level1_with_cleanup",
    "tasks" : [ 
        {
            "seq_no" : 1,
            "task_id" : "submit",
            "task_name" : "Work Order Initialization",
            "task_type" : "user",
            "roles" : [],
            "end_task" : false
        }, 
        {
            "seq_no" : 2,
            "task_id" : "aps_prevalidation",
            "task_name" : "Pre Validation",
            "task_type" : "service",
            "roles" : [],
            "end_task" : false
        }, 
        {
            "seq_no" : 3,
            "task_id" : "approval1",
            "task_name" : "Approval Level 1",
            "task_type" : "xor",
            "roles" : [ 
                "admin"
            ],
            "end_task" : false,
            "tags" : {
                "accept_caption" : "Approve",
                "permission" : {
                    "admin" : "RW",
                    "R" : [ 
                        "admin"
                    ]
                }
            },
            "email_detail" : {
                "pre_template" : "email_awaiting_approval",
                "post_template" : "email_approved"
            }
        }, 
        {
            "seq_no" : 4,
            "task_id" : "aps_prevalidation",
            "task_name" : "Pre Validation",
            "task_type" : "service",
            "roles" : [],
            "end_task" : false
        }, 
        {
            "seq_no" : 5,
            "task_id" : "approval2",
            "task_name" : "Approval Level 2",
            "task_flow" : {
                "Manual" : 6,
                "Auto" : 7
            },
            "task_type" : "xor",
            "roles" : [ 
                "Surya", 
                "admin", 
                "new_user"
            ],
            "end_task" : false,
            "tags" : {
                "accept_caption" : "Implement",
                "action" : "implement",
                "permission" : {
                    "admin" : "RW",
                    "R" : [ 
                        "admin"
                    ]
                }
            },
            "email_detail" : {
                "pre_template" : "email_awaiting_approval",
                "post_template" : "email_approved"
            }
        }, 
        {
            "seq_no" : 6,
            "task_id" : "aps_implementation",
            "task_name" : "Manual Implementation",
            "task_flow" : {
                "postvalidate" : 9
            },
            "task_type" : "service",
            "roles" : [],
            "end_task" : true,
            "email_detail" : {
                "post_template" : "email_implemented"
            }
        }, 
        {
            "seq_no" : 7,
            "task_id" : "ticket_validation",
            "task_name" : "Ticket Validation",
            "task_type" : "timer",
            "roles" : [],
            "end_task" : false
        }, 
        {
            "seq_no" : 8,
            "task_id" : "aps_implementation",
            "task_name" : "Auto Implementation",
            "task_flow" : {
                "postvalidate" : 9
            },
            "task_type" : "service",
            "roles" : [],
            "end_task" : true,
            "email_detail" : {
                "post_template" : "email_implemented"
            }
        }, 
        {
            "seq_no" : 9,
            "task_id" : "aps_postvalidation",
            "task_name" : "Post Validation",
            "task_type" : "service",
            "roles" : [],
            "end_task" : true
        }
    ],
    "~" : {
        "rejected" : {
            "seq_no" : 0,
            "task_id" : "aps_cleanup",
            "task_name" : "Cleanup Process",
            "task_type" : "service",
            "end_task" : false
        },
        "failed" : {
            "seq_no" : 0,
            "task_id" : "aps_cleanup",
            "task_name" : "Cleanup Process",
            "task_type" : "service",
            "end_task" : false
        },
        "not approved" : {
            "seq_no" : 0,
            "task_id" : "aps_cleanup",
            "task_name" : "Cleanup Process",
            "task_type" : "service",
            "end_task" : false
        }
    }
    })

    print "Successfully inserted the workflow in Data Base"
except Exception , e:
    print e
