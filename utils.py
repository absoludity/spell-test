DEFAULT_STATISTIC = {
    "right_count": 0,
    "total_count": 0,
    "last_attempt": None,
}


def order_words(words, stats):
    """Order with most wrong ones first."""
    # Should be a function of the time since last tested,
    # the number of times it's been tested, and
    # how easy it is.
    def weight(word):
        stat = stats.get(word, DEFAULT_STATISTIC)
        total = stat["total_count"]
        if total == 0:
            return 0
        return stat["right_count"] / float(total)

    return sorted(words, key=weight)
