"""merge sort module"""

# Walter Podewil
# CIS 226
# October 26, 2024

# This code was copied from David Barnes

# System Imports

# First Party Imports

# Third party Imports


class MergeSort:
    """MergeSort Class"""

    def __init__(self):
        # constructor
        self._aux = []

    # Main entry point to sort
    def sort(self, mergeable):
        """sort method"""
        self._aux = [None for i in range(len(mergeable))]
        self._sort(mergeable, 0, len(mergeable) - 1)

    # mergesort a[lo..hi] using auxiliary array aux[lo..hi]
    def _sort(self, mergeable, lo, hi):
        """recursive sort method"""
        if hi <= lo:
            return
        mid = lo + int((hi - lo) / 2)
        self._sort(mergeable, lo, mid)
        self._sort(mergeable, mid + 1, hi)
        self._merge(mergeable, lo, mid, hi)

    def _merge(self, mergeable, lo, mid, hi):
        """merge method"""
        # Copy to aux[]
        for k in range(lo, hi + 1):
            self._aux[k] = mergeable[k]

        # Merge back to iter[]
        i = lo
        j = mid + 1
        for k in range(lo, hi + 1):
            if i > mid:  # Index past left subarray max index
                mergeable[k] = self._aux[j]
                j += 1
            elif j > hi:  # index past right subarray max index
                mergeable[k] = self._aux[i]
                i += 1
            elif self._aux[j] < self._aux[i]:  # compare
                mergeable[k] = self._aux[j]
                j += 1
            else:
                mergeable[k] = self._aux[i]
                i += 1

        return
