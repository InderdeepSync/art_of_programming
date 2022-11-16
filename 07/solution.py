
from typing import List

def merge(meetings: List[List[int]]) -> List[List[int]]:
    meetings.sort(key=lambda m: m[0])

    merged = [meetings[0]]
    for meeting in meetings[1:]:
        meet_start, meet_end = meeting
        prev_meeting_start, prev_meeting_end = merged[-1]

        if meet_start > prev_meeting_end:
            merged.append(meeting)
        elif meet_end > prev_meeting_end:
            merged[-1] = [prev_meeting_start, meet_end]


    return merged