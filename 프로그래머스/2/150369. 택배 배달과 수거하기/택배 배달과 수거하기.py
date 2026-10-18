def solution(cap, n, deliveries, pickups):
    answer = 0
    dcap, pcap = 0,0
    
    for i in range(n-1, -1, -1):
        if deliveries[i]!=0 or pickups[i]!=0:
            cnt=0
            while deliveries[i]>dcap or pickups[i]>pcap:
                cnt+=1
                dcap+=cap
                pcap+=cap
            dcap -= deliveries[i]
            pcap -= pickups[i]
            answer += (i+1)*cnt*2
    return answer