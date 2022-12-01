from asyncio import get_event_loop, run

async def main():
    print('done!')

if __name__ ==  '__main__':
    # METHOD1
    # loop = get_event_loop()
    # loop.run_until_complete(main())

    # METHOD2
    run(main())