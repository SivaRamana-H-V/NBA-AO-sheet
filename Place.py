def XLPlace(A,TSN):
  TSn=int(TSN)
  S=[]
  for i in range(7,TSn+8):
    B="%s%s" %(A,i)
    S.append(B)
  return S
