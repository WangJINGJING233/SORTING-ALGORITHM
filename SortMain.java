package sort;

import sun.awt.windows.WPrinterJob;

public class SortMain {
    // 在数组中交换两个位置上的值
    public static void change(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void BubbleSort(int[] arr) {
        int length = arr.length;
        if (length < 2) {
            return;
        }
        for (int i = 0; i < length - 1; i++) {
            for (int j = 0; j < length - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    change(arr, j, j + 1);
                }
            }
        }
    }

    public static void SelectSort(int[] arr) {
        int length = arr.length;
        if (length < 2) {
            return;
        }
        for (int i = 0; i < length - 1; i++) {
            int min_idx = i;
            for (int j = i + 1; j < length; j++) {
                if (arr[j] < arr[min_idx]) {
                    min_idx = j;
                }
            }
            change(arr, i, min_idx);
        }
    }

    public static void QuickSort(int[] arr, int left, int right) {
        if (left >= right) {
            return;
        }
        int i = left, j = right;
        int val = arr[left];
        while (i < j) {
            while (i < j && arr[j] >= val) {
                j -= 1;
            }
            arr[i] = arr[j];
            while (i < j && arr[i] <= val) {
                i += 1;
            }
            arr[j] = arr[i];
        }
        arr[i] = val;
        QuickSort(arr, left, j - 1);
        QuickSort(arr, j + 1, right);

    }


    public static void InsertSort(int[] arr) {
        int length = arr.length;
        if (length < 2) {
            return;
        }
        for (int i = 1; i < length; i++) {
            int j = i;
            int val = arr[i];
            while (j >= 1 && arr[j - 1] > val) {
                change(arr, j, j - 1);
                j -= 1;
            }
        }
    }


    public static void ShellSort(int[] arr) {
        int length = arr.length;
        if (length < 2) {
            return;
        }
        int gap = length / 2;
        while (gap != 0) {
            for (int i = gap; i < length; i++) {
                int j = i;
                int val = arr[i];
                while (j >= gap && arr[j - gap] > val) {
                    change(arr, j, j - gap);
                    j -= gap;
                }
            }
            gap /= 2;
        }
    }


    public static int[] MergeSort(int[] arr) {
        int length = arr.length;
        if (length<2){
            return arr;
        }
        int mid = length/2;
        int[] leftArr = new int[mid];
        for (int i=0;i<mid;i++){
            leftArr[i] = arr[i];
        }
        int[] rightArr = new int[length-mid];
        for (int j=mid;j<length;j++){
            rightArr[j-mid] = arr[j];
        }
        int[] left = MergeSort(leftArr);
        int[] right = MergeSort(rightArr);
        return merge(left, right);
    }

    public static int[] merge(int[] left, int[] right) {
        int i = 0, j = 0;
        int ll = left.length, rl = right.length;
        int[] ret = new int[ll + rl];
        int idx = 0;
        while (i < ll && j < rl) {
            if (left[i] < right[j]) {
                ret[idx] = left[i];
                i += 1;
                idx += 1;
            } else {
                ret[idx] = right[j];
                j += 1;
                idx += 1;
            }
        }
        while (i < ll) {
            ret[idx] = left[i];
            i += 1;
            idx += 1;
        }
        while (j < rl) {
            ret[idx] = right[j];
            j += 1;
            idx += 1;
        }
        return ret;
    }


    public static void HeapSort(int[] arr){
        int length = arr.length;
        if (length<2){
            return;
        }
        for (int i=length/2-1;i>-1;i--){
            heapAdjust(arr,i,length);
        }
        for (int i=length-1;i>-1;i--){
            change(arr,i,0);
            heapAdjust(arr,0,i);
        }
    }

    public static void heapAdjust(int[] arr,int i,int length){
        int root = i;
        int left = 2*i+1;
        int right = 2*i+2;
        if (left<length && arr[root]<arr[left]){
            root = left;
        }
        if (right<length && arr[root]< arr[right]){
            root = right;
        }
        if (root!=i){
            change(arr,root,i);
            heapAdjust(arr,root,length);
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[]{5, 6, 2, 1, 3, 4, 9, 0, 7, 8};

//        System.out.println("BubbleSort");
//        BubbleSort(arr);

//        System.out.println("SelectSort");
//        SelectSort(arr);

//        System.out.println("QuickSort");
//        QuickSort(arr,0,arr.length-1);

//        System.out.println("InsertSort");
//        InsertSort(arr);

//        System.out.println("ShellSort");
//        ShellSort(arr);

//        System.out.println("MergeSort");
//        arr = MergeSort(arr);

//        System.out.println("HeapSort");
//        HeapSort(arr);


        for (int num : arr) {
            System.out.print(num + " ");
        }

    }
}
