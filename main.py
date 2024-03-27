# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

# <ProgramSnippet>
import asyncio
import configparser
from msgraph.generated.models.o_data_errors.o_data_error import ODataError
from graph import Graph

async def main():
    print('Python Graph Tutorial\n')

    # Load settings
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']

    graph: Graph = Graph(azure_settings)

    await greet_user(graph)

    await list_calendar_events(graph)
# </ProgramSnippet>

# <GreetUserSnippet>
async def greet_user(graph: Graph):
    user = await graph.get_user()
    if user:
        print('Hello,', user.display_name)
        # For Work/school accounts, email is in mail property
        # Personal accounts, email is in userPrincipalName
        print('Email:', user.mail or user.user_principal_name, '\n')
# </GreetUserSnippet>

# <DisplayAccessTokenSnippet>
async def display_access_token(graph: Graph):
    token = await graph.get_user_token()
    print('User token:', token, '\n')
# </DisplayAccessTokenSnippet>

# <ListCalendarEventsSnippet>
async def list_calendar_events(graph: Graph):
    # Assuming `get_calendar_events` is a method you've defined
    # in your Graph class to fetch calendar events.
    event_page = await graph.get_calendar_events()
    if event_page and event_page.value:
        # Output each event's details
        for event in event_page.value:
            print('Event:', event.subject)
            if event.start and event.start.date_time:
                print('  Start:', event.start.date_time)
            else:
                print('  Start: NONE')

            if event.end and event.end.date_time:
                print('  End:', event.end.date_time)
            else:
                print('  End: NONE')

            if event.location:
                print('  Location:', event.location.display_name or 'NONE')
            else:
                print('  Location: NONE')

            print('  Is All Day?:', 'Yes' if event.is_all_day else 'No')

        more_available = event_page.odata_next_link is not None
        print('\nMore events available?', more_available, '\n')
# </ListCalendarEventsSnippet>

# <MakeGraphCallSnippet>
async def make_graph_call(graph: Graph):
    await graph.make_graph_call()
# </MakeGraphCallSnippet>

# Run main
asyncio.run(main())
