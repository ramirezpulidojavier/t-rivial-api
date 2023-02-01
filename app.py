from fastapi import FastAPI, status
from routes.player_queue import queue
from routes.match import match
from routes.pot import pot
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="REST API with FastAPI and Mongodb",
    description="""
This is the API for T-rivial.
###### Designed with ❤️ by [Javier Ramírez](https://github.com/ramirezpulidojavier) and [Juan Carlos](https://github.com/JCCG-code)
---
#### Know more
You can take a look at both repositories, and know more, here:
* 👨‍💻 [T-rivial API](https://github.com/ramirezpulidojavier/T-rivial): the source code for this API.
* 🤖 [T-rivial Front](https://github.com/JCCG-code/T-rivial): the source code for the application that consumes this API.""",
    version="alpha-1.0",
    contact={
        'name': 'Javier Ramirez',
        'email': 'ramirezpulidojavier@gmail.com'
    }
)

app.include_router(queue)
app.include_router(match)
app.include_router(pot)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check")
async def health_check():
    return Response(status_code=status.HTTP_200_OK)
