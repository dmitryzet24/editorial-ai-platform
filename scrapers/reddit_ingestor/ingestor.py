import os
import asyncio
import json
from aiokafka import AIOKafkaProducer
import asyncpraw
from dotenv import load_dotenv

load_dotenv()


async def main():
    # Kafka
    producer = AIOKafkaProducer(
        bootstrap_servers=os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    )
    await producer.start()
    print("✅ Connect to Redpanda")

    # Reddit
    reddit = asyncpraw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )

    subreddit = await reddit.subreddit("knitting")
    print("🚀 Начинаем слушать Reddit (r/knitting)...")

    try:
        # Listening
        async for submission in subreddit.stream.submissions():
            data = {
                "id": submission.id,
                "title": submission.title,
                "author": str(submission.author),
                "url": submission.url,
                "score": submission.score,
                "created_utc": submission.created_utc
            }

            # Send to Redpanda
            await producer.send_and_wait(
                "raw_knitting_events",
                json.dumps(data).encode('utf-8')
            )
            print(f"Cought the post: {submission.title[:50]}...")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await producer.stop()


if __name__ == "__main__":
    asyncio.run(main())