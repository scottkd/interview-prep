def condense_meeting_times(meeting_times):
  """
  meeting_times - list of tuples of all individual meeting times

  returns condesnsed meeting time list of tuples
  """
  condensed_list = []

  for meeting in meeting_times:
    curr_start = meeting[0]
    curr_end = meeting[1]

    if len(condensed_list)==0:
      condensed_list.append(meeting)
      continue

    cnt = 0
    inserted = False

    for i in range(len(condensed_list)):
      iter_start = condensed_list[i][0]
      iter_end = condensed_list[i][1]

      if curr_end < iter_start:
        condensed_list.insert(cnt, meeting)
        inserted = True

      elif curr_start > iter_end:
        # go to next element
        if i == len(condensed_list) - 1:
          # last iter
          condensed_list.append(meeting)

      elif curr_start > iter_start and curr_end > iter_end:
        # adjust condensed range
        condensed_list[cnt] = (iter_start, curr_end)

      elif curr_start < iter_start and curr_end < iter_end:
        # adjust condensed range
        condensed_list[cnt] = (curr_start, iter_end)

      elif curr_start < iter_start and curr_end > iter_end:
        condensed_list[cnt] = (curr_start, curr_end)

      cnt += 1

  return condensed_list


