class Solution {
public:
int InversePairs(vector<int> data) {
        int length  = data.size();
        return mergeSort(data, 0, length-1);
    }
 
    int mergeSort(vector<int>& data, int start, int end) {
        // �ݹ���ֹ����
        if(start >= end) {
            return 0;
        }
 
        // �ݹ�
        int mid = (start + end) / 2;
        int leftCounts = mergeSort(data, start, mid);
        int rightCounts = mergeSort(data, mid+1, end);
 
        // �鲢���򣬲����㱾���������
        vector<int> copy(data); // ���鸱�������ڹ鲢����
        int foreIdx = mid;      // ǰ�벿�ֵ�ָ��
        int backIdx = end;      // ��벿�ֵ�ָ��
        int counts = 0;         // ��¼�����������
        int idxCopy = end;      // ����������±�
        while(foreIdx>=start && backIdx >= mid+1) {
            if(data[foreIdx] > data[backIdx]) {
                copy[idxCopy--] = data[foreIdx--];
                counts += backIdx - mid;
            } else {
                copy[idxCopy--] = data[backIdx--];
            }
        }
        while(foreIdx >= start) {
            copy[idxCopy--] = data[foreIdx--];
        }
        while(backIdx >= mid+1) {
            copy[idxCopy--] = data[backIdx--];
        }
        for(int i=start; i<=end; i++) {
            data[i] = copy[i];
        }
 
        return (leftCounts+rightCounts+counts);
    }

};