#include <iostream>
#include <stdio.h>
#include <unistd.h>
#include <opencv2/opencv.hpp>
#include "/home/ironman/work/lib/cpp/custom.h"

using namespace cv;
using namespace std;

// Can be optimized for space using unordered_set
bool isPresent[256][256][256];
vector<Vec3b> color_list;

void initialize(Mat& image) {
    // assuming the starting pixel (0,0) belongs to background
    Vec3b a = image.at<Vec3b>(0, 0);
    color_list.pb(a);
    isPresent[a[0]][a[1]][a[2]] = true;
}

Mat fillGaps(Mat& image) {
    Mat image_floodfill;
    image.copyTo(image_floodfill);
    floodFill(image_floodfill, Point(0,0), Vec3b(255, 255, 255));

    Mat image_inv_floodfill;
    bitwise_not(image_floodfill, image_inv_floodfill);

    Mat out = (image | image_inv_floodfill);
    return out;
}

void getShape(Mat &image) {
    Mat image_gray;
    cvtColor(image, image_gray, CV_BGR2GRAY);
    vector<vector<Point> > contours;
    findContours(image_gray, contours, RETR_LIST, CHAIN_APPROX_SIMPLE, Point(0,0));

    for (int i = 0; i < contours.size(); i++) {
        vector<Point> result;
        approxPolyDP(contours[i], result, arcLength(contours[i], true) * 0.01, true);
        int size = result.size();
        switch (size) {
            case 3:
                cout << "triangle" << endl; break;
            case 4:
                cout << "quadrilateral" << endl; break;
            case 5:
                cout << "pentagon" << endl; break;
            case 6:
                cout << "hexagon" << endl; break;
            case 7:
                cout << "heptagon" << endl; break;
            case 8:
                cout << "octagon" << endl; break;
            default:
                cout << "circle" << endl; break;
        }
    }
}

int main(int argc, char const *argv[])
{
    if (argc != 2) {
        printf("usage: getShapes.out <image_name>\n");
        return -1;
    }

    Mat image = imread(argv[1]);
    if (!image.data) {
        printf("No such image: %s found\n", argv[1]);
        return -1;
    }

    initialize(image);

    int r = image.rows, c = image.cols;
    for (int i = 0; i < r; ++i) {
        for (int j = 0; j < c; ++j) {
            Vec3b a = image.at<Vec3b>(i, j);
            if (!isPresent[a[0]][a[1]][a[2]]) {
                isPresent[a[0]][a[1]][a[2]] = true;
                color_list.pb(a);
            }
        }
    }

    cout << "Colors present: " << color_list << endl;
    int l = color_list.size();

    for (int k = 1; k < l; k++) { // Skip the first color as it is white
        Mat test = image.clone();
        Vec3b &color = color_list[k];
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                Vec3b &a = test.at<Vec3b>(i, j);
                if (a != color)
                    a[0] = a[1] = a[2] = 0;
                else
                    a[0] = a[1] = a[2] = 255;
            }
        }
        cout << "Color: " << color << endl;
        Mat output = fillGaps(test);
        getShape(output);
    }

    return 0;
}
