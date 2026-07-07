f=open("url.txt","r")
f2=open("output.txt","a+")
# protocols=""


while True:
    dt=f.readline()
    dt = dt.strip()
    # global protocols
    protocols=""
    if(dt==""):
        break
    for x in dt:
        if(x==':'):
            break
        protocols+=x
    if protocols == "https":
        
        f2.write(dt+"  -->  "+"https             'secured' \n")
    elif protocols=="http":
         f2.write(dt+"  -->  "+"http             'not secured' \n")
    else:
        f2.write(dt+"  -->  "+"unknown protocol  'not secured' \n")

    