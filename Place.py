def XLPlace(A,TSN):
  TSN=TSN
  S=[]
  for i in range(7,TSN+1):
    B="%s%s" %(A,i)
    S.append(B)
  return S
