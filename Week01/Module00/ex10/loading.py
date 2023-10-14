import time


def ft_progress(lst):
    total = len(lst)
    start_time = time.time()
    max_bar_length = 50

    for i, elem in enumerate(lst, start=1):
        yield elem
        elapsed_time = time.time() - start_time
        remaining_time = (elapsed_time / i) * (total - i)
        percent_complete = i / total * 100
        bar_length = int(percent_complete / 100 * max_bar_length)
        progress_bar = "[" + "=" * bar_length + " " * (max_bar_length - bar_length) + "]"
        loading_info = f"{i}/{total}"
        eta_info = f"ETA: {remaining_time:.2f}s"
        elapsed_info = f"elapsed time {elapsed_time:.2f}s"

        combined_info = "{:<12} {} | {:<14} {}".format(eta_info, progress_bar, loading_info, elapsed_info)
        print("\r" + combined_info, end="")

        time.sleep(0.01)
    print()


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
print(ret)
