import socket
from datetime import datetime

# 서버의 IP와 PORT 설정
server_ip = "192.168.1.10"
server_port = 9001
server_addr_port = (server_ip, server_port)

buffersize = 52

# 소켓을 UDP로 열고 서버의 IP/PORT를 연결
udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket.bind(server_addr_port)

print("UDP server is up and listening")

while True:
    try:
        # 클라이언트로부터 데이터 수신
        byte_addr_pair = udp_server_socket.recvfrom(buffersize)
        msg = byte_addr_pair[0]
        addr = byte_addr_pair[1]

        try:
            # 수신한 비트 배열을 정수로 변환
            vcuCode = int.from_bytes(msg[0:4], byteorder='little')
            ccmCode = int.from_bytes(msg[4:8], byteorder='little')
            brkCode = int.from_bytes(msg[8:12], byteorder='little')
            aclCode = int.from_bytes(msg[12:16], byteorder='little')
            amlCode = int.from_bytes(msg[16:20], byteorder='little')
            bcuCode = int.from_bytes(msg[20:24], byteorder='little')
            seatCode = int.from_bytes(msg[24:28], byteorder='little')
            airbagCode = int.from_bytes(msg[28:32], byteorder='little')
            accCode = int.from_bytes(msg[32:36], byteorder='little')
            aebCode = int.from_bytes(msg[36:40], byteorder='little')
            scuCode = int.from_bytes(msg[40:44], byteorder='little')
            hmiCode = int.from_bytes(msg[44:48], byteorder='little')
            cluCode = int.from_bytes(msg[48:52], byteorder='little')

            # 파일에 코드값 기록
            with open("DTC_Result.txt", "a") as file:
                # 현재 시간 기록
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"DTC time: {current_time}\n")

                file.write(f"VCU Code: {vcuCode if vcuCode != 4294967295 else 'Not Received'}\n")
                file.write(f"CCM Code: {ccmCode if ccmCode != 4294967295 else 'Not Received'}\n")
                file.write(f"BRK Code: {brkCode if brkCode != 4294967295 else 'Not Received'}\n")
                file.write(f"ACL Code: {aclCode if aclCode != 4294967295 else 'Not Received'}\n")
                file.write(f"AML Code: {amlCode if amlCode != 4294967295 else 'Not Received'}\n")
                file.write(f"BCU Code: {bcuCode if bcuCode != 4294967295 else 'Not Received'}\n")
                file.write(f"SEAT Code: {seatCode if seatCode != 4294967295 else 'Not Received'}\n")
                file.write(f"AIRBAG Code: {airbagCode if airbagCode != 4294967295 else 'Not Received'}\n")
                file.write(f"ACC Code: {accCode if accCode != 4294967295 else 'Not Received'}\n")
                file.write(f"AEB Code: {aebCode if aebCode != 4294967295 else 'Not Received'}\n")
                file.write(f"SCU Code: {scuCode if scuCode != 4294967295 else 'Not Received'}\n")
                file.write(f"HMI Code: {hmiCode if hmiCode != 4294967295 else 'Not Received'}\n")
                file.write(f"CLU Code: {cluCode if cluCode != 4294967295 else 'Not Received'}\n")
                file.write("----------------------------\n\n")

            print(f"Client IP Address: {addr}")
        except ValueError:
            print("Error")

    except BlockingIOError:
        continue
