def condense_meeting_times(meeting_times):
  """
  meeting_times - list of tuples of all individual meeting times

  returns condesnsed meeting time list of tuples
  """
  condensed_list = []

  for meeting in meeting_times:
    
    if len(condensed_list)==0:
      condensed_list.append(meeting)
      continue
    
    curr_start = meeting[0]
    curr_end = meeting[1]

    for i in range(len(condensed_list)):
      iter_start = condensed_list[i][0]
      iter_end = condensed_list[i][1]

      if curr_end < iter_start:
        # add meeting to condensed list
        condensed_list.insert(i, meeting)

      elif curr_start > iter_end:
        # start is greater than current window
        if i == len(condensed_list) - 1:
          # last iter, add element to the end
          condensed_list.append(meeting)

      elif curr_start > iter_start and curr_end > iter_end:
        # adjust end of range
        condensed_list[i] = (iter_start, curr_end)

      elif curr_start < iter_start and curr_end < iter_end:
        # adjust start of range
        condensed_list[i] = (curr_start, iter_end)

      elif curr_start < iter_start and curr_end > iter_end:
        # adjust start and end of range
        condensed_list[i] = (curr_start, curr_end)


  return condensed_list

assert condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) ==   [(0, 1), (3, 8), (9, 12)]
