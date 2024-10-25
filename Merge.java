package searchalgorithms.searchclasses;

import java.util.Arrays;

//copied from another project, which was originally copied from princeton's algorithm
public class Merge {
    // Merge class for integers

    // prevents class from instantiation
    private Merge() {
    }

    private static void merge(Integer[] inputArray, Integer[] auxillaryArray, int min, int mid, int max) {

        // copy inputArray to auxillaryArray
        for (int arrayIndex = min; arrayIndex <= max; arrayIndex++) {
            auxillaryArray[arrayIndex] = inputArray[arrayIndex];
        }

        // merge subarrays to inputArray
        int subarrayOneIndex = min;
        int subarrayTwoIndex = mid + 1;
        for (int arrayIndex = min; arrayIndex <= max; arrayIndex++) {
            if (subarrayOneIndex > mid) {
                inputArray[arrayIndex] = auxillaryArray[subarrayTwoIndex++];
            } else if (subarrayTwoIndex > max) {
                inputArray[arrayIndex] = auxillaryArray[subarrayOneIndex++];
            } else if (isLessThan(auxillaryArray[subarrayTwoIndex], auxillaryArray[subarrayOneIndex])) {

                inputArray[arrayIndex] = auxillaryArray[subarrayTwoIndex++];

            } else {
                inputArray[arrayIndex] = auxillaryArray[subarrayOneIndex++];
            }
        }
        // post condition
        // assert isSorted(inputArray, min, max);

    }

    public static void sort(Integer[] inputArray) {
        Integer[] auxillaryArray = new Integer[inputArray.length];
        sort(inputArray, auxillaryArray, 0, inputArray.length - 1);

    }

    private static void sort(Integer[] inputArray, Integer[] auxillaryArray, int min, int max) {
        if (max <= min) {
            return;
        }
        int mid = min + (max - min) / 2;
        sort(inputArray, auxillaryArray, min, mid);
        sort(inputArray, auxillaryArray, mid + 1, max);
        merge(inputArray, auxillaryArray, min, mid, max);
    }

    // is leftcomparable less than rightcomparable
    private static boolean isLessThan(Integer left, Integer right) {
        boolean check = left.compareTo(right) < 0;
        return check;
    }

    // check if array is sorted
    private static boolean isSorted(Integer[] myArray) {
        return isSorted(myArray, 0, myArray.length - 1);
    }

    private static boolean isSorted(Integer[] myArray, int min, int max) {
        for (int index = min; index < max; index++) {
            if (isLessThan(myArray[index + 1], myArray[index])) {
                return false;
            }
        }
        return true;
    }

}