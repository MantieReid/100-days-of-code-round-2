
def rob( nums: List[int]) -> int:
  last, now = 0, 0

  for i in nums: last, now = now, max(last + i, now)

  print(now)


  return now


