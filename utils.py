import json
import httpx


def extract_json_from_string(text: str) -> dict:
    """
    Extract JSON content from a string and parse it into a Python dictionary.

    Args:
        text (str): Input string that may contain JSON content

    Returns:
        dict: Parsed JSON as dictionary if found, empty dict if no valid JSON
    """
    try:
        # Find the first '{' and last '}' to locate potential JSON content
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            json_str = text[start : end + 1]
            return json.loads(json_str)
        return {}

    except json.JSONDecodeError:
        # Return empty dict if JSON parsing fails
        return {}


async def get_event_data():
    return {
        "organization": "TFUG Bhubaneswar",
        "pastEvents": [
            {
                "title": "AI Day",
                "date": "27th October 2024",
                "time": "9:00 AM to 3:00 PM",
                "venue": "IIIT Bhubaneswar",
                "rsvpCount": 220,
                "speakers": [
                    {
                        "name": "Biswanath Giri",
                        "designation": "Google Cloud Principal Architect",
                        "isGDE": True,
                        "talk": "Securing Gen AI Application",
                        "social": {
                            "linkedin": "https://www.linkedin.com/in/biswanathgiri"
                        },
                        "tags": ["AI", "ML", "Security"],
                    },
                    {
                        "name": "Ashutosh S. Bhakare",
                        "designation": "CEO at Unnati Development and Training Centre Pvt Ltd",
                        "isGDE": True,
                        "talk": "Demensifying AI on GKE",
                        "social": {"linkedin": "https://www.linkedin.com/in/abhakare"},
                        "tags": ["AI", "ML", "Security"],
                    },
                    {
                        "name": "Atanu Sarkar",
                        "designation": "Senior Engineer @Bosch(BGSW)",
                        "talk": "Answering questions across modalities for saving lives",
                        "isGDE": False,
                        "social": {
                            "linkedin": "https://www.linkedin.com/in/mratanusarkar/"
                        },
                        "tags": ["AI"],
                    },
                    {
                        "name": "Pankaj Rai",
                        "designation": "Sr Engr Cslt-App Dev Verizon | Android, Firebase, Machine Learning",
                        "talk": "Super power your app with Genkit",
                        "isGDE": True,
                        "social": {
                            "linkedin": "https://in.linkedin.com/in/pankajrai16"
                        },
                        "tags": ["AI", "ML", "Android", "Firebase"],
                    },
                    {
                        "name": "Priyadarshi Sadangi",
                        "designation": "Chief Operating Officer, Emerging Tech Centre of Excellence, STPI",
                        "talk": "Use of AI in PSU",
                        "isGDE": False,
                        "social": {"linkedin": "https://www.linkedin.com/in/psadangi/"},
                        "tags": ["AI", "PSU"],
                    },
                    {
                        "name": "Dr. Sujata Chakravarty",
                        "designation": "Dean SoET, CEO Data Science & Machine Learning Research Centre, Professor Dept. of CSE at Centurion University of Technology & Management, Bhubaneswar, Odisha",
                        "talk": "Pioneering AI Advancements: Leveraging Technology for a Better Tomorrow",
                        "isGDE": False,
                        "social": {
                            "linkedin": "https://www.linkedin.com/in/dr-sujata-chakravarty-2390184a/"
                        },
                        "tags": ["Data Science", "AI"],
                    },
                ],
                "agenda": [
                    {
                        "text": "Check-in & Registration",
                        "startTime": "8:30 AM",
                        "endTime": "10:00 AM",
                        "icon": "📝",
                    },
                    {
                        "text": "Welcome and Introduction by TFUG Bhubaneswar",
                        "startTime": "10:00 AM",
                        "endTime": "10:25 AM",
                        "icon": "👋",
                    },
                    {
                        "text": "Demensifying AI on GKE",
                        "startTime": "10:30 AM",
                        "endTime": "11:15 AM",
                        "speaker": "Ashutosh S. Bhakare",
                        "designation": "CEO at Unnati Development and Training Centre Pvt Ltd",
                        "icon": "🤖",
                    },
                    {
                        "text": "Superpower Your App with Genkit",
                        "startTime": "11:20 AM",
                        "endTime": "12:05 PM",
                        "speaker": "Pankaj Rai",
                        "designation": "Sr Engr Cslt-App Dev Verizon | Android, Firebase, Machine Learning",
                        "icon": "⚡️",
                    },
                    {
                        "text": "Engagement & Refreshments",
                        "startTime": "12:05 PM",
                        "endTime": "12:25 PM",
                        "icon": "🍵",
                    },
                    {
                        "text": "Securing Gen AI Application",
                        "startTime": "12:25 PM",
                        "endTime": "01:10 PM",
                        "speaker": "Biswanath Giri",
                        "designation": "Google Cloud Principal Architect",
                        "icon": "🔐",
                    },
                    {
                        "text": "Pioneering AI Advancements: Leveraging Technology for a Better Tomorrow",
                        "startTime": "01:15 PM",
                        "endTime": "01:45 PM",
                        "speaker": "Dr. Sujata Chakravarty",
                        "designation": "",
                        "icon": "👩‍🏫",
                    },
                    {
                        "text": "Lunch & Refreshments",
                        "startTime": "01:45 PM",
                        "endTime": "02:45 PM",
                        "icon": "🍽️",
                    },
                    {
                        "text": "Answering Questions Across Modalities for Saving Lives",
                        "startTime": "02:45 PM",
                        "endTime": "03:30 PM",
                        "speaker": "Atanu Sarkar",
                        "designation": "Senior Engineer @Bosch(BGSW)",
                        "icon": "🩺",
                    },
                    {
                        "text": "Use of AI in PSU",
                        "startTime": "03:35 PM",
                        "endTime": "04:05 PM",
                        "speaker": "Priyadarshi Sadangi",
                        "designation": "Chief Operating Officer, Emerging Tech Centre of Excellence, STPI",
                        "icon": "🏢",
                    },
                    {
                        "text": "Felicitation & Thank You Note by TFUG Bhubaneswar",
                        "startTime": "04:10 PM",
                        "endTime": "04:30 PM",
                        "icon": "🎉",
                    },
                ],
            },
            {
                "title": "The Eras of Large Language Models by TFUG Bhubaneswar",
                "shortDescription": "The Eras of Large Language Models by TFUG Bhubaneswar is an event series featuring workshops, seminars, and competitions focused on the evolution and applications of LLMs.",
                "mode": "Hybrid",
                "date": "August'24 to September'24",
                "location": "IIIT Bhubaneswar",
                "description": "Welcome to the Eras of LLMs event series, organized by TFUG Bhubaneswar. This event is dedicated to bringing together enthusiasts, experts, and learners to explore and celebrate the advancements in machine learning and large language models. Join us for a series of workshops, seminars, and competitions that delve into the latest trends and innovations in the field.",
                "features": [
                    {
                        "text": "Workshops",
                        "description": "Hands-on sessions to learn about LLMs, their architecture, and practical applications.",
                    },
                    {
                        "text": "Seminars",
                        "description": "Expert talks and presentations on the latest research and developments in the field of LLMs.",
                    },
                    {
                        "text": "Competitions",
                        "description": "Exciting competitions to challenge your skills and knowledge in LLMs and machine learning.",
                    },
                ],
                "speakers": [
                    {
                        "name": "Tarun R Jain",
                        "designation": "ML @AI Planet, GDE in AI/ML",
                    },
                    {
                        "name": "Sangram Rath",
                        "designation": "Cloud Architect & Technology Advisor at OD10",
                    },
                    {
                        "name": "Dr. Subrata Kumar Mohanty",
                        "designation": "Asst Prof at IIIT Bhubaneswar",
                    },
                ],
            },
            {
                "title": "The Eras of Large Language Models",
                "date": "14th September 2024",
                "mode": "offline",
                "location": "IIIT Bhubaneswar",
                "speakers": [
                    {
                        "name": "Tarun R Jain",
                        "designation": "ML @AI Planet, GDE in AI/ML",
                    },
                    {
                        "name": "Sangram Rath",
                        "designation": "Cloud Architect & Technology Advisor at OD10",
                    },
                    {
                        "name": "Dr. Subrata Kumar Mohanty",
                        "designation": "Asst Prof at IIIT Bhubaneswar",
                    },
                ],
            },
            {
                "title": "Build with Gemini ✨",
                "date": "01 September 2024",
                "mode": "online",
                "location": "youtube",
                "speaker": "Swoyam Siddarth",
                "designation": "AI Intern @ fiXit",
                "attendees": "150+",
            },
            {
                "title": "Getting Started with Gemini ✨",
                "date": "24 August 2024",
                "mode": "online",
                "location": "youtube",
                "speaker": "Saswat Samal",
                "designation": "Data Scientist, Ernst & Young GDS",
                "attendees": "200+",
            },
            {
                "title": "Applications using LLM",
                "date": "10 August 2024",
                "mode": "offline",
                "location": "KIIT Bhubaneswar",
                "speaker": "Puspanjali Mohapatra",
                "designation": "Assistant Professor (CSE) at IIIT Bhubaneswar",
                "attendees": "180+",
            },
            {
                "title": "Exploring LLMs & ChatBot",
                "date": "11 February 2024",
                "mode": "online",
                "location": "youtube",
                "shortDescription": "Dive into the world of language models at our event! Unleash ChatBot potential in just one immersive experience.",
            },
            {
                "title": "Keras Community Day",
                "date": "30 September 2023",
                "mode": "online",
                "location": "youtube",
                "shortDescription": "Keras Community Day is a series of events focused on Keras and machine learning, led by machine learning communities around the world.",
                "speakers": [
                    {
                        "name": "Vrijraj Singh",
                        "designation": "Tech Lead, agprop\nCommunity Organizer, Techferment\nGDE for Firebase and Web",
                    },
                    {
                        "name": "Anish Kumar",
                        "designation": "AI Software Engineering Manager, Intel",
                    },
                    {
                        "name": "Suryansu Dash",
                        "designation": "Data Science Manager, Newton School",
                    },
                ],
            },
            {
                "title": "Google IO Extended Bhubaneswar",
                "date": "22 July 2022",
                "location": "Trident College, BBSR",
                "shortDescription": "Google I/O Extended 2023 Bhubaneswar",
            },
        ],
    }


async def get_team_data():
    return {
        "teamMembers": [
            {
                "name": "Saswat Samal",
                "designation": "Data Scientist at EY GDS",
                "photo": "/data/Team/member1.webp",
                "social": {
                    "instagram": "https://www.instagram.com/basicallysaswat",
                    "linkedin": "https://www.linkedin.com/in/saswatsamal/",
                    "github": "https://github.com/saswatsamal",
                },
            },
            {
                "name": "Sanket Sanjeeb Pattanaik",
                "designation": "Data Scientist at EY India",
                "photo": "/data/Team/member2.webp",
                "social": {
                    "instagram": "https://www.instagram.com/sanket_pattanaik/",
                    "linkedin": "https://www.linkedin.com/in/sanket-sanjeeb-pattanaik-96706b1a7/",
                },
            },
            {
                "name": "Aman Patanaik",
                "designation": "Programmer Analyst Trainee at Cognizant",
                "photo": "/data/Team/member3.webp",
                "social": {
                    "linkedin": "https://www.linkedin.com/in/aman-patnaik-7384bb20a/"
                },
            },
            {
                "name": "Swoyam Siddharth Nayak",
                "designation": "AI Intern @ fiXit",
                "photo": "/data/Team/member5.webp",
                "social": {
                    "instagram": "https://www.instagram.com/_swoyamsiddharth_/",
                    "linkedin": "https://www.linkedin.com/in/swoyam2609/",
                    "github": "http://github.com/Swoyam2609/",
                },
            },
            {
                "name": "Prince Pious Omm Prakash",
                "designation": "IIIT Bhubaneswar",
                "photo": "/data/Team/member7.webp",
                "social": {
                    "linkedin": "https://www.linkedin.com/in/prince03/",
                    "instagram": "https://www.instagram.com/__prince.x__",
                },
            },
            {
                "name": "Chakit Sharma",
                "designation": "Vellore Institute of Technology",
                "photo": "/data/Team/member4.webp",
                "social": {
                    "instagram": "https://www.instagram.com/developer_chakit/",
                    "linkedin": "https://www.linkedin.com/in/chakitsharma28/",
                    "github": "https://github.com/geekchakit/",
                },
            },
            {
                "name": "Smruti Ranjan Nayak",
                "designation": "Frontend Developer & UI/UX Designer",
                "photo": "/data/Team/member6.webp",
                "social": {
                    "instagram": "https://www.instagram.com/sm8uti",
                    "linkedin": "https://www.linkedin.com/in/smruti-ranjan-nayak/",
                    "github": "https://github.com/SM8UTI",
                },
            },
        ]
    }
