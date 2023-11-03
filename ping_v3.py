#  dziala na 75%

num_committees = int(input())
num_seats = int(input())

committee_data = []
total_votes = 0

for _ in range(num_committees):
    committee_type, committee_name, votes = input().split()
    committee_data.append((committee_type, committee_name, float(votes)))
    total_votes += committee_data[-1][2]

committee_seats = [0] * num_committees
divisor_committees = [1.0] * num_committees
take_seat = [False] * num_committees

for i in range(num_committees):
    if committee_data[i][0].lower() in ("kw", "kkw"):
        if committee_data[i][2] / total_votes >= 0.05 if committee_data[i][0].lower() == "kw" else 0.08:
            take_seat[i] = True

while num_seats:
    largest_committee = 0
    current_committee = 1

    for i in range(num_committees):
        if take_seat[i]:
            largest_committee = i
            if i == num_committees - 1:
                break
            current_committee = i + 1
            break

    while current_committee < num_committees:
        if take_seat[current_committee] and committee_data[current_committee][2] > committee_data[largest_committee][2]:
            largest_committee = current_committee
        current_committee += 1

    committee_seats[largest_committee] += 1
    num_seats -= 1

    committee_data[largest_committee] = (
        committee_data[largest_committee][0],
        committee_data[largest_committee][1],
        committee_data[largest_committee][2] / divisor_committees[largest_committee],
    )
    divisor_committees[largest_committee] += 1.0

for i in range(num_committees):
    print(
        f"{committee_data[i][0]} {committee_data[i][1]} {committee_seats[i]}"
    )