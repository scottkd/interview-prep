def condense_meeting_times(meeting_times):
  """
  meeting_times - list of tuples of all individual meeting times

  returns condesnsed meeting time list of tuples
  """
  condensed_list = []

  for meeting in meeting_times:
    
    if len(condensed_list)==0:
      # add first element
      condensed_list.append(meeting)
      continue
    
    curr_start = meeting[0]
    curr_end = meeting[1]

    for i in range(len(condensed_list)):
      start_check = condensed_list[i][0]
      end_check = condensed_list[i][1]

      if curr_end < start_check:
        # add meeting to condensed list
        condensed_list.insert(i, meeting)

      elif curr_start > end_check:
        # start is greater than current window
        if i == len(condensed_list) - 1:
          # last item, add element to the end
          condensed_list.append(meeting)

      elif curr_start > start_check and curr_end > end_check:
        # adjust end of range
        condensed_list[i] = (start_check, curr_end)

      elif curr_start < start_check and curr_end < end_check:
        # adjust start of range
        condensed_list[i] = (curr_start, end_check)

      elif curr_start < start_check and curr_end > end_check:
        # adjust start and end of range
        condensed_list[i] = (curr_start, curr_end)


  return condensed_list

assert condense_meeting_times(  [(1, 2), (2, 3)]) ==   [(1, 3)]
assert condense_meeting_times(  [(1, 5), (2, 3)]) ==   [(1, 5)]
assert condense_meeting_times(  [(1, 10), (2, 6), (3, 5), (7, 9)]) ==   [(1, 10)]
assert condense_meeting_times([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) ==   [(0, 1), (3, 8), (9, 12)]
  

def cmt_optimized(meeting_times):
  """
  meeting_times - list of tuples of all individual meeting times

  returns condesnsed meeting time list of tuples
  """
  condensed_list = []

  sorted_times = sorted(meeting_times)

  for i in range(len(sorted_times) - 1):
    curr_item = sorted_times[i]
    next_item = sorted_times[i+1]

    if curr_item[1] < next_item[0]:
      condensed_list.append(curr_item)  

    else:
      sorted_times[i+1] = ( curr_item[0], max(curr_item[1], next_item[1]) )


    if i == (len(sorted_times) - 1) - 1:
      condensed_list.append(sorted_times[i+1])  

  return condensed_list



assert cmt_optimized(  [(1, 2), (2, 3)]) ==   [(1, 3)], cmt_optimized(  [(1, 2), (2, 3)])
assert cmt_optimized(  [(1, 5), (2, 3)]) ==   [(1, 5)]
assert cmt_optimized(  [(1, 10), (2, 6), (3, 5), (7, 9)]) ==   [(1, 10)]
assert cmt_optimized([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]) ==   [(0, 1), (3, 8), (9, 12)]