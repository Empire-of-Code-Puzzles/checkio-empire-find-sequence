"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [
                [1, 2, 1, 1],
                [1, 1, 4, 1],
                [1, 3, 1, 6],
                [1, 7, 2, 5]
            ],
            "answer": True,
            "explanation": [
                [0, 0],
                [1, 0],
                [2, 0],
                [3, 0]
            ]
        },
        {
            "input": [
                [7, 1, 4, 1],
                [1, 2, 5, 2],
                [3, 4, 1, 3],
                [1, 1, 8, 1]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [2, 1, 1, 6, 1],
                [1, 3, 2, 1, 1],
                [4, 1, 1, 3, 1],
                [5, 5, 5, 5, 5],
                [1, 1, 3, 1, 1]
            ],
            "answer": True,
            "explanation": [
                [3, 0],
                [3, 1],
                [3, 2],
                [3, 3]
            ]
        },
        {
            "input": [
                [7, 1, 1, 8, 1, 1],
                [1, 1, 7, 3, 1, 5],
                [2, 3, 1, 2, 5, 1],
                [1, 1, 1, 5, 1, 4],
                [4, 6, 5, 1, 3, 1],
                [1, 1, 9, 1, 2, 1]
            ],
            "answer": True,
            "explanation": [
                [1, 5],
                [2, 4],
                [3, 3],
                [4, 2]
            ]
        },
        {
            "input": [
                [2, 6, 2, 2, 7, 6, 5],
                [3, 4, 8, 7, 7, 3, 6],
                [6, 7, 3, 1, 2, 4, 1],
                [2, 5, 7, 6, 3, 2, 2],
                [3, 4, 3, 2, 7, 5, 6],
                [8, 4, 6, 5, 2, 9, 7],
                [5, 8, 3, 1, 3, 7, 8]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [1, 7, 6, 1, 8, 5, 1],
                [7, 9, 1, 7, 2, 8, 6],
                [5, 1, 4, 5, 8, 8, 3],
                [8, 6, 3, 9, 7, 6, 9],
                [9, 8, 9, 8, 6, 8, 2],
                [1, 7, 2, 4, 9, 3, 8],
                [9, 9, 8, 6, 9, 2, 6]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [6, 9, 1, 1, 6, 2],
                [5, 9, 7, 8, 2, 5],
                [2, 1, 1, 7, 9, 8],
                [1, 8, 1, 4, 7, 4],
                [7, 8, 5, 4, 5, 1],
                [6, 4, 8, 8, 1, 8]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [2, 7, 6, 2, 1, 5, 2, 8, 4, 4],
                [8, 7, 5, 8, 9, 2, 8, 9, 5, 5],
                [5, 7, 7, 7, 4, 1, 1, 2, 6, 8],
                [4, 6, 6, 3, 2, 7, 6, 6, 5, 1],
                [2, 6, 6, 9, 8, 5, 5, 6, 7, 7],
                [9, 4, 1, 9, 1, 3, 7, 2, 3, 1],
                [5, 1, 4, 3, 6, 5, 9, 3, 4, 1],
                [6, 5, 5, 1, 7, 7, 8, 2, 1, 1],
                [9, 5, 7, 8, 2, 9, 2, 6, 9, 3],
                [8, 2, 5, 7, 3, 7, 3, 8, 6, 2]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [1, 9, 7, 8, 9, 3, 6, 5, 6, 2],
                [4, 9, 4, 8, 3, 4, 8, 8, 5, 9],
                [2, 8, 5, 5, 7, 8, 6, 1, 3, 6],
                [6, 4, 7, 6, 9, 1, 4, 5, 7, 8],
                [4, 7, 7, 9, 8, 8, 8, 8, 4, 4],
                [3, 7, 3, 2, 1, 9, 1, 8, 9, 1],
                [4, 7, 2, 4, 8, 1, 2, 3, 6, 2],
                [4, 4, 1, 3, 3, 3, 9, 2, 6, 7],
                [8, 6, 1, 9, 3, 5, 8, 1, 7, 5],
                [7, 3, 6, 5, 3, 6, 6, 4, 8, 2]
            ],
            "answer": True,
            "explanation": [
                [4, 4],
                [4, 5],
                [4, 6],
                [4, 7]
            ]
        },
        {
            "input": [
                [1, 6, 1, 7],
                [4, 7, 3, 6],
                [3, 5, 7, 9],
                [8, 6, 6, 9]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [1, 2, 4, 6, 3],
                [2, 5, 2, 6, 3],
                [8, 7, 5, 9, 5],
                [2, 1, 1, 4, 3],
                [4, 2, 7, 5, 1]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [2, 3, 6, 5, 6, 2, 8, 3, 7, 4],
                [6, 9, 5, 9, 7, 6, 8, 5, 1, 6],
                [6, 8, 2, 6, 1, 9, 3, 6, 6, 4],
                [5, 8, 3, 2, 3, 8, 7, 4, 6, 4],
                [2, 3, 1, 4, 5, 1, 2, 5, 6, 9],
                [5, 4, 8, 7, 5, 5, 8, 4, 9, 5],
                [9, 7, 9, 9, 5, 9, 9, 8, 1, 2],
                [5, 1, 7, 4, 8, 3, 4, 1, 8, 8],
                [5, 3, 3, 2, 6, 1, 4, 3, 8, 8],
                [4, 8, 1, 4, 5, 8, 8, 7, 4, 7]
            ],
            "answer": True,
            "explanation": [
                [5, 6],
                [6, 7],
                [7, 8],
                [8, 9]
            ]
        },
        {
            "input": [
                [7, 7, 4, 4, 8],
                [7, 4, 5, 5, 6],
                [6, 6, 5, 2, 8],
                [6, 2, 3, 8, 4],
                [6, 1, 3, 1, 2]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [7, 9, 1, 7, 6, 7, 5, 9, 6],
                [5, 5, 9, 3, 1, 6, 7, 4, 7],
                [1, 7, 5, 2, 3, 1, 6, 4, 7],
                [2, 2, 2, 8, 7, 2, 6, 6, 9],
                [5, 6, 4, 2, 6, 7, 3, 4, 7],
                [5, 5, 6, 4, 9, 4, 3, 1, 7],
                [7, 3, 2, 3, 2, 4, 4, 7, 3],
                [3, 6, 9, 7, 2, 5, 6, 2, 5],
                [4, 1, 3, 9, 4, 2, 4, 8, 4]
            ],
            "answer": True,
            "explanation": [
                [0, 4],
                [1, 5],
                [2, 6],
                [3, 7]
            ]
        }
    ],
    "Extra": [
        {
            "input": [
                [6, 6, 7, 4, 4, 6, 7, 9, 7, 9],
                [4, 1, 8, 4, 7, 3, 5, 1, 1, 6],
                [6, 1, 8, 8, 9, 3, 7, 6, 8, 9],
                [8, 8, 7, 1, 6, 2, 1, 4, 1, 6],
                [4, 4, 9, 9, 8, 8, 5, 4, 9, 8],
                [5, 8, 1, 6, 8, 7, 1, 2, 9, 7],
                [1, 8, 2, 7, 8, 9, 8, 1, 7, 1],
                [7, 2, 7, 3, 7, 4, 3, 7, 1, 3],
                [7, 3, 8, 7, 5, 2, 8, 9, 2, 2],
                [5, 6, 4, 3, 1, 5, 5, 9, 2, 9]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [1, 5, 6, 3, 7, 3, 2],
                [2, 9, 1, 1, 5, 3, 8],
                [3, 3, 3, 1, 1, 8, 9],
                [4, 2, 1, 3, 2, 1, 4],
                [1, 4, 5, 7, 1, 3, 6],
                [4, 5, 8, 6, 1, 1, 2],
                [3, 7, 1, 5, 7, 4, 7]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [4, 7, 8, 2, 8, 9],
                [2, 1, 8, 4, 4, 8],
                [3, 9, 6, 4, 5, 6],
                [5, 8, 8, 7, 1, 4],
                [1, 6, 1, 5, 2, 1],
                [7, 5, 7, 2, 8, 7]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [[1, 5, 4, 4],
                      [2, 2, 4, 1],
                      [1, 4, 3, 5],
                      [4, 3, 3, 2]],
            "answer": True,
            "explanation": [
                [0, 3],
                [1, 2],
                [2, 1],
                [3, 0],
            ]
        },

        {
            "input": [
                [2, 8, 4, 9, 4, 8, 8, 7],
                [5, 2, 6, 9, 2, 2, 9, 3],
                [7, 8, 6, 9, 5, 9, 6, 9],
                [2, 2, 4, 6, 4, 2, 3, 1],
                [8, 7, 2, 6, 3, 1, 9, 4],
                [8, 6, 9, 6, 1, 5, 5, 6],
                [8, 7, 2, 7, 8, 5, 1, 7],
                [5, 1, 7, 9, 6, 2, 7, 6]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [7, 7, 1, 3],
                [6, 4, 8, 5],
                [7, 4, 6, 7],
                [6, 4, 4, 4]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [2, 8, 7, 2],
                [7, 7, 6, 7],
                [2, 8, 2, 1],
                [8, 2, 5, 2]
            ],
            "answer": False,
            "explanation": []
        },
        {
            "input": [
                [2, 6, 2, 3, 5, 2, 4, 8, 7],
                [5, 7, 8, 5, 9, 5, 7, 3, 4],
                [6, 4, 1, 2, 1, 6, 5, 8, 5],
                [9, 3, 1, 3, 5, 4, 6, 4, 8],
                [9, 6, 6, 8, 1, 9, 1, 2, 1],
                [5, 5, 5, 8, 6, 5, 3, 2, 5],
                [7, 5, 2, 9, 2, 9, 8, 2, 5],
                [5, 8, 1, 9, 1, 2, 6, 2, 2],
                [7, 5, 3, 6, 1, 6, 9, 5, 9]
            ],
            "answer": True,
            "explanation": [
                [4, 7],
                [5, 7],
                [6, 7],
                [7, 7]
            ]
        },
        {
            "input": [
                [1, 1, 2, 4, 6, 4, 1, 4],
                [3, 3, 4, 9, 9, 1, 9, 9],
                [2, 6, 7, 2, 7, 8, 8, 8],
                [5, 7, 8, 6, 5, 6, 3, 1],
                [7, 7, 4, 4, 1, 7, 8, 1],
                [2, 5, 7, 9, 7, 5, 8, 6],
                [1, 5, 3, 7, 2, 1, 6, 3],
                [1, 1, 3, 7, 7, 4, 9, 7]
            ],
            "answer": True,
            "explanation": [
                [4, 1],
                [5, 2],
                [6, 3],
                [7, 4]
            ]
        },
        {
            "input": [
                [5, 2, 1, 4, 8, 3, 6],
                [3, 9, 7, 8, 6, 2, 5],
                [2, 8, 8, 4, 2, 5, 1],
                [5, 3, 9, 9, 5, 6, 3],
                [6, 2, 1, 4, 5, 8, 6],
                [2, 3, 2, 7, 5, 7, 4],
                [1, 6, 5, 1, 5, 2, 3]
            ],
            "answer": True,
            "explanation": [
                [3, 4],
                [4, 4],
                [5, 4],
                [6, 4]
            ]
        },
        {
            "input": [
                [2, 4, 1, 7],
                [1, 2, 4, 1],
                [9, 4, 2, 1],
                [5, 9, 2, 2]
            ],
            "answer": True,
            "explanation": [
                [0, 0],
                [1, 1],
                [2, 2],
                [3, 3]
            ]
        },
        {
            "input": [
                [3, 2, 9, 9, 2, 7, 6, 3],
                [4, 8, 9, 9, 9, 9, 3, 3],
                [9, 6, 7, 5, 9, 9, 4, 2],
                [1, 5, 9, 9, 6, 7, 8, 2],
                [9, 9, 3, 4, 8, 9, 8, 1],
                [4, 1, 8, 5, 5, 7, 8, 9],
                [6, 5, 6, 3, 4, 3, 1, 6],
                [4, 4, 5, 3, 9, 4, 4, 3]
            ],
            "answer": True,
            "explanation": [
                [1, 2],
                [1, 3],
                [1, 4],
                [1, 5]
            ]
        },
        {
            "input": [
                [1, 1, 7, 2, 8, 1, 9, 2, 6, 2],
                [3, 7, 6, 6, 7, 4, 7, 5, 3, 7],
                [2, 4, 8, 5, 3, 9, 4, 9, 4, 4],
                [3, 1, 4, 9, 8, 9, 5, 3, 6, 8],
                [4, 5, 6, 4, 7, 3, 9, 9, 9, 9],
                [7, 7, 6, 4, 8, 9, 2, 3, 5, 7],
                [9, 1, 2, 1, 1, 7, 9, 2, 6, 5],
                [5, 7, 6, 9, 5, 3, 5, 4, 1, 9],
                [5, 4, 7, 8, 9, 3, 1, 4, 5, 1],
                [9, 5, 7, 9, 4, 7, 9, 5, 8, 8]
            ],
            "answer": True,
            "explanation": [
                [4, 6],
                [4, 7],
                [4, 8],
                [4, 9]
            ]
        },
        {
            "input": [
                [1, 1, 7, 2, 8, 1, 9, 2, 6, 2],
                [3, 7, 6, 6, 7, 4, 7, 5, 3, 7],
                [2, 4, 8, 5, 3, 9, 4, 9, 4, 4],
                [3, 1, 4, 9, 8, 9, 5, 3, 6, 8],
                [4, 5, 6, 4, 7, 3, 9, 1, 9, 9],
                [7, 7, 6, 4, 8, 9, 2, 3, 5, 7],
                [9, 1, 2, 1, 1, 7, 9, 2, 6, 4],
                [5, 7, 6, 9, 5, 3, 5, 4, 4, 9],
                [5, 4, 7, 8, 9, 3, 1, 4, 5, 1],
                [9, 5, 7, 9, 4, 7, 4, 5, 8, 8]
            ],
            "answer": True,
            "explanation": [
                [9, 6],
                [8, 7],
                [7, 8],
                [6, 9]
            ]
        }
    ]
}