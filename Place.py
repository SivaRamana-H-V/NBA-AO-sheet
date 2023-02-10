def XLPlace(A,TSN):
  TSn=int(TSN)
  S=[]
  for i in range(7,TSN+1):
    B="%s%s" %(A,i)
    S.append(B)
  return S
