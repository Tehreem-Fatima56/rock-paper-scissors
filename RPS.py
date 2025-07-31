def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return "R"

    prediction = predict_next_move(opponent_history, 3)
    return counter_move(prediction)

def predict_next_move(history, length):
    recent = history[-length:]
    patterns = {}
    for i in range(len(history) - length):
        if history[i:i+length] == recent:
            next_move = history[i + length]
            patterns[next_move] = patterns.get(next_move, 0) + 1
    if patterns:
        return max(patterns, key=patterns.get)
    else:
        return max(set(history), key=history.count)

def counter_move(move):
    beats = {"R": "P", "P": "S", "S": "R"}
    return beats[move]
