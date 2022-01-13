def predict(V1, V2, V3, V4):
    if V1 <= 6.5:
        if V2 <= 4.5:
            if V4 <= 17.0:
                if V4 <= 2.5:
                    if V3 <= 375.0:
                        return [[27.0, 6.0]]
                    else:  # if V3 > 375.0
                        return [[3.0, 0.0]]
                else:  # if V4 > 2.5
                    if V4 <= 3.5:
                        return [[0.0, 1.0]]
                    else:  # if V4 > 3.5
                        if V2 <= 1.5:
                            return [[27.0, 8.0]]
                        else:  # if V2 > 1.5
                            if V4 <= 12.0:
                                if V1 <= 1.0:
                                    return [[2.0, 0.0]]
                                else:  # if V1 > 1.0
                                    if V1 <= 5.0:
                                        if V3 <= 625.0:
                                            if V4 <= 6.5:
                                                if V1 <= 3.0:
                                                    return [[4.0, 3.0]]
                                                else:  # if V1 > 3.0
                                                    return [[6.0, 3.0]]
                                            else:  # if V4 > 6.5
                                                if V4 <= 10.5:
                                                    if V1 <= 3.0:
                                                        return [[1.0, 1.0]]
                                                    else:  # if V1 > 3.0
                                                        return [[1.0, 1.0]]
                                                else:  # if V4 > 10.5
                                                    return [[4.0, 3.0]]
                                        else:  # if V3 > 625.0
                                            if V4 <= 10.0:
                                                if V1 <= 3.0:
                                                    return [[0.0, 3.0]]
                                                else:  # if V1 > 3.0
                                                    return [[1.0, 1.0]]
                                            else:  # if V4 > 10.0
                                                return [[2.0, 0.0]]
                                    else:  # if V1 > 5.0
                                        return [[0.0, 1.0]]
                            else:  # if V4 > 12.0
                                if V3 <= 625.0:
                                    return [[5.0, 0.0]]
                                else:  # if V3 > 625.0
                                    if V1 <= 5.0:
                                        if V4 <= 15.0:
                                            if V2 <= 3.5:
                                                return [[2.0, 0.0]]
                                            else:  # if V2 > 3.5
                                                if V1 <= 3.0:
                                                    return [[1.0, 2.0]]
                                                else:  # if V1 > 3.0
                                                    return [[0.0, 1.0]]
                                        else:  # if V4 > 15.0
                                            if V2 <= 3.5:
                                                if V1 <= 3.0:
                                                    return [[0.0, 1.0]]
                                                else:  # if V1 > 3.0
                                                    return [[2.0, 1.0]]
                                            else:  # if V2 > 3.5
                                                if V1 <= 3.0:
                                                    return [[5.0, 1.0]]
                                                else:  # if V1 > 3.0
                                                    return [[1.0, 0.0]]
                                    else:  # if V1 > 5.0
                                        return [[1.0, 0.0]]
            else:  # if V4 > 17.0
                if V4 <= 24.5:
                    return [[12.0, 0.0]]
                else:  # if V4 > 24.5
                    if V4 <= 25.5:
                        return [[0.0, 1.0]]
                    else:  # if V4 > 25.5
                        if V3 <= 625.0:
                            if V4 <= 48.5:
                                return [[7.0, 0.0]]
                            else:  # if V4 > 48.5
                                if V4 <= 51.5:
                                    return [[0.0, 1.0]]
                                else:  # if V4 > 51.5
                                    return [[2.0, 0.0]]
                        else:  # if V3 > 625.0
                            if V1 <= 2.5:
                                if V2 <= 3.5:
                                    if V4 <= 36.5:
                                        return [[1.0, 0.0]]
                                    else:  # if V4 > 36.5
                                        if V4 <= 45.0:
                                            return [[0.0, 1.0]]
                                        else:  # if V4 > 45.0
                                            if V4 <= 63.5:
                                                return [[1.0, 0.0]]
                                            else:  # if V4 > 63.5
                                                if V4 <= 76.0:
                                                    return [[0.0, 1.0]]
                                                else:  # if V4 > 76.0
                                                    return [[1.0, 0.0]]
                                else:  # if V2 > 3.5
                                    return [[6.0, 0.0]]
                            else:  # if V1 > 2.5
                                if V3 <= 875.0:
                                    return [[4.0, 0.0]]
                                else:  # if V3 > 875.0
                                    if V4 <= 44.5:
                                        if V1 <= 3.5:
                                            return [[0.0, 1.0]]
                                        else:  # if V1 > 3.5
                                            if V4 <= 42.0:
                                                if V4 <= 37.5:
                                                    if V4 <= 30.0:
                                                        return [[1.0, 1.0]]
                                                    else:  # if V4 > 30.0
                                                        return [[0.0, 1.0]]
                                                else:  # if V4 > 37.5
                                                    return [[1.0, 0.0]]
                                            else:  # if V4 > 42.0
                                                return [[0.0, 1.0]]
                                    else:  # if V4 > 44.5
                                        return [[1.0, 0.0]]
        else:  # if V2 > 4.5
            if V4 <= 49.5:
                if V3 <= 3625.0:
                    if V4 <= 18.5:
                        if V4 <= 13.0:
                            return [[0.0, 3.0]]
                        else:  # if V4 > 13.0
                            if V4 <= 14.5:
                                if V3 <= 1375.0:
                                    return [[0.0, 1.0]]
                                else:  # if V3 > 1375.0
                                    if V2 <= 6.5:
                                        return [[2.0, 0.0]]
                                    else:  # if V2 > 6.5
                                        return [[0.0, 1.0]]
                            else:  # if V4 > 14.5
                                if V2 <= 5.5:
                                    if V1 <= 3.0:
                                        return [[2.0, 2.0]]
                                    else:  # if V1 > 3.0
                                        return [[0.0, 3.0]]
                                else:  # if V2 > 5.5
                                    return [[0.0, 5.0]]
                    else:  # if V4 > 18.5
                        if V3 <= 1625.0:
                            if V4 <= 42.0:
                                if V4 <= 40.0:
                                    if V1 <= 4.5:
                                        if V2 <= 5.5:
                                            if V1 <= 3.5:
                                                if V4 <= 29.5:
                                                    return [[3.0, 0.0]]
                                                else:  # if V4 > 29.5
                                                    if V4 <= 33.5:
                                                        return [[0.0, 1.0]]
                                                    else:  # if V4 > 33.5
                                                        return [[3.0, 0.0]]
                                            else:  # if V1 > 3.5
                                                if V4 <= 34.5:
                                                    if V4 <= 33.5:
                                                        if V4 <= 30.5:
                                                            if V4 <= 27.0:
                                                                if V4 <= 24.5:
                                                                    return [[1.0, 1.0]]
                                                                else:  # if V4 > 24.5
                                                                    return [[0.0, 1.0]]
                                                            else:  # if V4 > 27.0
                                                                return [[1.0, 0.0]]
                                                        else:  # if V4 > 30.5
                                                            return [[0.0, 1.0]]
                                                    else:  # if V4 > 33.5
                                                        return [[1.0, 0.0]]
                                                else:  # if V4 > 34.5
                                                    return [[0.0, 1.0]]
                                        else:  # if V2 > 5.5
                                            if V4 <= 21.5:
                                                return [[1.0, 0.0]]
                                            else:  # if V4 > 21.5
                                                if V4 <= 38.5:
                                                    if V4 <= 36.5:
                                                        if V4 <= 29.0:
                                                            if V1 <= 3.0:
                                                                if V4 <= 27.0:
                                                                    if V4 <= 24.0:
                                                                        return [[1.0, 1.0]]
                                                                    else:  # if V4 > 24.0
                                                                        return [[1.0, 1.0]]
                                                                else:  # if V4 > 27.0
                                                                    return [[1.0, 2.0]]
                                                            else:  # if V1 > 3.0
                                                                return [[0.0, 2.0]]
                                                        else:  # if V4 > 29.0
                                                            if V1 <= 3.0:
                                                                return [[0.0, 1.0]]
                                                            else:  # if V1 > 3.0
                                                                if V4 <= 32.5:
                                                                    return [[1.0, 0.0]]
                                                                else:  # if V4 > 32.5
                                                                    return [[2.0, 1.0]]
                                                    else:  # if V4 > 36.5
                                                        return [[0.0, 1.0]]
                                                else:  # if V4 > 38.5
                                                    return [[1.0, 0.0]]
                                    else:  # if V1 > 4.5
                                        return [[1.0, 0.0]]
                                else:  # if V4 > 40.0
                                    return [[0.0, 2.0]]
                            else:  # if V4 > 42.0
                                if V3 <= 1375.0:
                                    if V1 <= 3.0:
                                        return [[0.0, 1.0]]
                                    else:  # if V1 > 3.0
                                        return [[1.0, 0.0]]
                                else:  # if V3 > 1375.0
                                    return [[5.0, 0.0]]
                        else:  # if V3 > 1625.0
                            if V3 <= 2625.0:
                                if V4 <= 21.5:
                                    return [[1.0, 0.0]]
                                else:  # if V4 > 21.5
                                    if V4 <= 48.5:
                                        if V2 <= 9.5:
                                            if V3 <= 2125.0:
                                                if V4 <= 30.5:
                                                    if V4 <= 28.5:
                                                        if V1 <= 3.0:
                                                            return [[0.0, 2.0]]
                                                        else:  # if V1 > 3.0
                                                            if V4 <= 27.0:
                                                                if V4 <= 25.5:
                                                                    if V4 <= 23.5:
                                                                        return [[0.0, 1.0]]
                                                                    else:  # if V4 > 23.5
                                                                        return [[1.0, 0.0]]
                                                                else:  # if V4 > 25.5
                                                                    return [[0.0, 2.0]]
                                                            else:  # if V4 > 27.0
                                                                return [[2.0, 0.0]]
                                                    else:  # if V4 > 28.5
                                                        return [[1.0, 0.0]]
                                                else:  # if V4 > 30.5
                                                    return [[0.0, 10.0]]
                                            else:  # if V3 > 2125.0
                                                if V4 <= 27.0:
                                                    return [[0.0, 2.0]]
                                                else:  # if V4 > 27.0
                                                    if V4 <= 39.0:
                                                        if V1 <= 3.0:
                                                            return [[1.0, 0.0]]
                                                        else:  # if V1 > 3.0
                                                            if V4 <= 33.0:
                                                                return [[1.0, 1.0]]
                                                            else:  # if V4 > 33.0
                                                                return [[0.0, 1.0]]
                                                    else:  # if V4 > 39.0
                                                        return [[2.0, 0.0]]
                                        else:  # if V2 > 9.5
                                            return [[0.0, 6.0]]
                                    else:  # if V4 > 48.5
                                        return [[1.0, 0.0]]
                            else:  # if V3 > 2625.0
                                if V4 <= 30.0:
                                    if V3 <= 3000.0:
                                        return [[4.0, 0.0]]
                                    else:  # if V3 > 3000.0
                                        return [[0.0, 1.0]]
                                else:  # if V4 > 30.0
                                    if V1 <= 1.5:
                                        return [[2.0, 0.0]]
                                    else:  # if V1 > 1.5
                                        if V2 <= 13.5:
                                            if V4 <= 43.5:
                                                return [[0.0, 5.0]]
                                            else:  # if V4 > 43.5
                                                if V4 <= 46.5:
                                                    return [[1.0, 1.0]]
                                                else:  # if V4 > 46.5
                                                    return [[0.0, 1.0]]
                                        else:  # if V2 > 13.5
                                            if V4 <= 44.0:
                                                return [[2.0, 0.0]]
                                            else:  # if V4 > 44.0
                                                return [[0.0, 1.0]]
                else:  # if V3 > 3625.0
                    return [[0.0, 6.0]]
            else:  # if V4 > 49.5
                if V3 <= 3125.0:
                    if V2 <= 10.5:
                        if V1 <= 2.5:
                            if V4 <= 58.5:
                                if V4 <= 57.5:
                                    return [[3.0, 0.0]]
                                else:  # if V4 > 57.5
                                    return [[0.0, 1.0]]
                            else:  # if V4 > 58.5
                                return [[9.0, 0.0]]
                        else:  # if V1 > 2.5
                            return [[15.0, 0.0]]
                    else:  # if V2 > 10.5
                        if V4 <= 80.5:
                            if V4 <= 62.5:
                                return [[2.0, 0.0]]
                            else:  # if V4 > 62.5
                                if V4 <= 72.5:
                                    return [[0.0, 2.0]]
                                else:  # if V4 > 72.5
                                    if V1 <= 3.0:
                                        return [[0.0, 1.0]]
                                    else:  # if V1 > 3.0
                                        return [[2.0, 0.0]]
                        else:  # if V4 > 80.5
                            return [[6.0, 0.0]]
                else:  # if V3 > 3125.0
                    if V3 <= 6250.0:
                        if V4 <= 57.5:
                            return [[0.0, 3.0]]
                        else:  # if V4 > 57.5
                            if V1 <= 3.5:
                                if V3 <= 3375.0:
                                    return [[0.0, 1.0]]
                                else:  # if V3 > 3375.0
                                    return [[8.0, 0.0]]
                            else:  # if V1 > 3.5
                                if V1 <= 4.5:
                                    if V4 <= 63.5:
                                        return [[1.0, 0.0]]
                                    else:  # if V4 > 63.5
                                        if V3 <= 3750.0:
                                            return [[1.0, 0.0]]
                                        else:  # if V3 > 3750.0
                                            return [[0.0, 5.0]]
                                else:  # if V1 > 4.5
                                    return [[3.0, 0.0]]
                    else:  # if V3 > 6250.0
                        if V2 <= 43.5:
                            return [[0.0, 5.0]]
                        else:  # if V2 > 43.5
                            if V3 <= 11250.0:
                                return [[1.0, 0.0]]
                            else:  # if V3 > 11250.0
                                return [[0.0, 2.0]]
    else:  # if V1 > 6.5
        if V1 <= 14.5:
            if V4 <= 15.5:
                if V2 <= 2.5:
                    if V4 <= 12.5:
                        if V2 <= 1.5:
                            if V1 <= 10.0:
                                return [[3.0, 0.0]]
                            else:  # if V1 > 10.0
                                return [[12.0, 2.0]]
                        else:  # if V2 > 1.5
                            return [[5.0, 0.0]]
                    else:  # if V4 > 12.5
                        if V2 <= 1.5:
                            return [[16.0, 0.0]]
                        else:  # if V2 > 1.5
                            if V1 <= 12.5:
                                return [[1.0, 0.0]]
                            else:  # if V1 > 12.5
                                return [[8.0, 1.0]]
                else:  # if V2 > 2.5
                    if V1 <= 12.0:
                        return [[3.0, 0.0]]
                    else:  # if V1 > 12.0
                        if V3 <= 1000.0:
                            return [[0.0, 1.0]]
                        else:  # if V3 > 1000.0
                            return [[1.0, 0.0]]
            else:  # if V4 > 15.5
                if V4 <= 23.5:
                    if V1 <= 13.5:
                        if V4 <= 16.5:
                            if V1 <= 8.5:
                                return [[2.0, 0.0]]
                            else:  # if V1 > 8.5
                                if V1 <= 12.0:
                                    if V3 <= 1625.0:
                                        if V1 <= 9.5:
                                            return [[0.0, 1.0]]
                                        else:  # if V1 > 9.5
                                            if V2 <= 2.5:
                                                return [[1.0, 0.0]]
                                            else:  # if V2 > 2.5
                                                if V1 <= 10.5:
                                                    return [[1.0, 0.0]]
                                                else:  # if V1 > 10.5
                                                    return [[0.0, 2.0]]
                                    else:  # if V3 > 1625.0
                                        return [[1.0, 0.0]]
                                else:  # if V1 > 12.0
                                    return [[1.0, 0.0]]
                        else:  # if V4 > 16.5
                            return [[9.0, 0.0]]
                    else:  # if V1 > 13.5
                        if V4 <= 17.5:
                            return [[1.0, 0.0]]
                        else:  # if V4 > 17.5
                            if V2 <= 3.5:
                                if V2 <= 2.5:
                                    return [[0.0, 1.0]]
                                else:  # if V2 > 2.5
                                    if V4 <= 20.0:
                                        return [[0.0, 1.0]]
                                    else:  # if V4 > 20.0
                                        return [[1.0, 0.0]]
                            else:  # if V2 > 3.5
                                return [[0.0, 2.0]]
                else:  # if V4 > 23.5
                    if V2 <= 7.5:
                        if V4 <= 63.0:
                            if V4 <= 61.5:
                                if V4 <= 27.5:
                                    return [[14.0, 0.0]]
                                else:  # if V4 > 27.5
                                    if V4 <= 51.5:
                                        if V3 <= 625.0:
                                            if V1 <= 12.5:
                                                return [[0.0, 1.0]]
                                            else:  # if V1 > 12.5
                                                if V4 <= 32.0:
                                                    return [[1.0, 0.0]]
                                                else:  # if V4 > 32.0
                                                    return [[1.0, 1.0]]
                                        else:  # if V3 > 625.0
                                            if V4 <= 50.5:
                                                if V4 <= 28.5:
                                                    if V1 <= 12.5:
                                                        return [[3.0, 0.0]]
                                                    else:  # if V1 > 12.5
                                                        if V3 <= 875.0:
                                                            return [[1.0, 0.0]]
                                                        else:  # if V3 > 875.0
                                                            if V2 <= 4.5:
                                                                return [[0.0, 1.0]]
                                                            else:  # if V2 > 4.5
                                                                return [[1.0, 1.0]]
                                                else:  # if V4 > 28.5
                                                    if V4 <= 36.0:
                                                        return [[14.0, 0.0]]
                                                    else:  # if V4 > 36.0
                                                        if V4 <= 40.5:
                                                            if V1 <= 12.5:
                                                                if V4 <= 39.0:
                                                                    if V4 <= 37.5:
                                                                        if V3 <= 1000.0:
                                                                            return [[1.0, 0.0]]
                                                                        else:  # if V3 > 1000.0
                                                                            if V2 <= 6.0:
                                                                                return [[0.0, 1.0]]
                                                                            else:  # if V2 > 6.0
                                                                                return [[1.0, 0.0]]
                                                                    else:  # if V4 > 37.5
                                                                        return [[2.0, 0.0]]
                                                                else:  # if V4 > 39.0
                                                                    return [[0.0, 1.0]]
                                                            else:  # if V1 > 12.5
                                                                return [[2.0, 0.0]]
                                                        else:  # if V4 > 40.5
                                                            return [[7.0, 0.0]]
                                            else:  # if V4 > 50.5
                                                if V3 <= 1375.0:
                                                    return [[0.0, 1.0]]
                                                else:  # if V3 > 1375.0
                                                    return [[1.0, 0.0]]
                                    else:  # if V4 > 51.5
                                        return [[11.0, 0.0]]
                            else:  # if V4 > 61.5
                                return [[0.0, 1.0]]
                        else:  # if V4 > 63.0
                            return [[16.0, 0.0]]
                    else:  # if V2 > 7.5
                        if V3 <= 2125.0:
                            if V1 <= 9.5:
                                return [[0.0, 2.0]]
                            else:  # if V1 > 9.5
                                if V4 <= 49.0:
                                    if V1 <= 12.0:
                                        if V4 <= 43.5:
                                            if V4 <= 40.0:
                                                return [[1.0, 0.0]]
                                            else:  # if V4 > 40.0
                                                return [[0.0, 1.0]]
                                        else:  # if V4 > 43.5
                                            return [[2.0, 0.0]]
                                    else:  # if V1 > 12.0
                                        return [[3.0, 0.0]]
                                else:  # if V4 > 49.0
                                    if V4 <= 62.0:
                                        if V4 <= 51.0:
                                            return [[1.0, 1.0]]
                                        else:  # if V4 > 51.0
                                            return [[0.0, 1.0]]
                                    else:  # if V4 > 62.0
                                        return [[1.0, 0.0]]
                        else:  # if V3 > 2125.0
                            if V4 <= 71.5:
                                if V1 <= 10.0:
                                    if V3 <= 2625.0:
                                        return [[7.0, 0.0]]
                                    else:  # if V3 > 2625.0
                                        if V3 <= 3125.0:
                                            return [[0.0, 1.0]]
                                        else:  # if V3 > 3125.0
                                            return [[1.0, 0.0]]
                                else:  # if V1 > 10.0
                                    return [[14.0, 0.0]]
                            else:  # if V4 > 71.5
                                if V2 <= 10.0:
                                    return [[0.0, 2.0]]
                                else:  # if V2 > 10.0
                                    if V4 <= 75.0:
                                        return [[0.0, 1.0]]
                                    else:  # if V4 > 75.0
                                        if V4 <= 82.5:
                                            if V4 <= 78.5:
                                                return [[2.0, 0.0]]
                                            else:  # if V4 > 78.5
                                                return [[0.0, 1.0]]
                                        else:  # if V4 > 82.5
                                            return [[5.0, 0.0]]
        else:  # if V1 > 14.5
            if V2 <= 4.5:
                if V4 <= 26.5:
                    if V2 <= 2.5:
                        if V1 <= 19.5:
                            return [[21.0, 0.0]]
                        else:  # if V1 > 19.5
                            if V4 <= 22.5:
                                if V4 <= 21.5:
                                    if V2 <= 1.5:
                                        return [[15.0, 1.0]]
                                    else:  # if V2 > 1.5
                                        return [[1.0, 1.0]]
                                else:  # if V4 > 21.5
                                    return [[0.0, 1.0]]
                            else:  # if V4 > 22.5
                                if V3 <= 375.0:
                                    return [[15.0, 1.0]]
                                else:  # if V3 > 375.0
                                    return [[9.0, 0.0]]
                    else:  # if V2 > 2.5
                        if V1 <= 18.5:
                            if V4 <= 22.0:
                                if V4 <= 20.0:
                                    return [[1.0, 0.0]]
                                else:  # if V4 > 20.0
                                    return [[1.0, 1.0]]
                            else:  # if V4 > 22.0
                                return [[2.0, 0.0]]
                        else:  # if V1 > 18.5
                            return [[1.0, 1.0]]
                else:  # if V4 > 26.5
                    return [[51.0, 0.0]]
            else:  # if V2 > 4.5
                if V1 <= 25.5:
                    if V1 <= 20.5:
                        if V1 <= 16.5:
                            if V2 <= 7.5:
                                if V4 <= 84.0:
                                    if V4 <= 45.0:
                                        if V4 <= 34.0:
                                            return [[3.0, 0.0]]
                                        else:  # if V4 > 34.0
                                            if V3 <= 1375.0:
                                                return [[0.0, 1.0]]
                                            else:  # if V3 > 1375.0
                                                if V4 <= 36.5:
                                                    return [[1.0, 1.0]]
                                                else:  # if V4 > 36.5
                                                    return [[3.0, 0.0]]
                                    else:  # if V4 > 45.0
                                        return [[5.0, 0.0]]
                                else:  # if V4 > 84.0
                                    if V4 <= 90.0:
                                        return [[0.0, 1.0]]
                                    else:  # if V4 > 90.0
                                        return [[1.0, 0.0]]
                            else:  # if V2 > 7.5
                                return [[10.0, 0.0]]
                        else:  # if V1 > 16.5
                            if V4 <= 82.0:
                                return [[0.0, 2.0]]
                            else:  # if V4 > 82.0
                                return [[1.0, 0.0]]
                    else:  # if V1 > 20.5
                        return [[20.0, 0.0]]
                else:  # if V1 > 25.5
                    return [[0.0, 1.0]]