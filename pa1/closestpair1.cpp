#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <climits>

using namespace std;

struct Point {
    double x, y;
};

pair<Point, Point> closestPair(vector<Point>& points);
double euclideanDistance(const Point& a, const Point& b);
pair<Point, Point> closestPairInLine(vector<Point>& points, double distance);
bool sortByY(const Point& a, const Point& b);
pair<Point, Point> bruteForce(vector<Point>& points);

void readPoints(vector<Point>& points) {
    int n;
    cin >> n;
    points.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> points[i].x >> points[i].y;
    }
}

void printResult(const pair<Point, Point>& result) {
    cout << fixed << setprecision(4);
    cout << result.first.x << " " << result.first.y << " "
         << result.second.x << " " << result.second.y << endl;
}

int main() {
    vector<Point> points;
    while (true) {
        readPoints(points);
        if (points.empty()) break;

        pair<Point, Point> result = closestPair(points);
        printResult(result);
    }
    return 0;
}

pair<Point, Point> closestPair(vector<Point>& points) {
    if (points.size() == 1) {
        return {Point{INT_MIN, INT_MIN}, Point{INT_MAX, INT_MAX}};
    }
    if (points.size() == 2) {
        return {points[0], points[1]};
    }
    if (points.size() == 3) {
        return bruteForce(points);
    }

    sort(points.begin(), points.end(), [](const Point& a, const Point& b) {
        return a.x < b.x;
    });

    int mid = points.size() / 2;
    vector<Point> leftPoints(points.begin(), points.begin() + mid);
    vector<Point> rightPoints(points.begin() + mid, points.end());

    pair<Point, Point> pair1 = closestPair(leftPoints);
    pair<Point, Point> pair2 = closestPair(rightPoints);

    double dist1 = euclideanDistance(pair1.first, pair1.second);
    double dist2 = euclideanDistance(pair2.first, pair2.second);
    double minDist = min(dist1, dist2);

    vector<Point> strip;
    for (const auto& point : points) {
        if (abs(point.x - points[mid].x) < minDist) {
            strip.push_back(point);
        }
    }
    sort(strip.begin(), strip.end(), sortByY);

    pair<Point, Point> pair3 = closestPairInLine(strip, minDist);
    double dist3 = euclideanDistance(pair3.first, pair3.second);

    if (dist3 < minDist) {
        return pair3;
    } else if (dist1 < dist2) {
        return pair1;
    } else {
        return pair2;
    }
}

pair<Point, Point> closestPairInLine(vector<Point>& points, double distance) {
    pair<Point, Point> closestPair(Point{INT_MIN, INT_MIN}, Point{INT_MAX, INT_MAX});
    double minDist = distance;

    for (int i = 0; i < points.size(); ++i) {
        for (int j = i + 1; j < points.size() && points[j].y - points[i].y < minDist; ++j) {
            double dist = euclideanDistance(points[j], points[i]);
            if (dist < minDist) {
                closestPair = {points[i], points[j]};
                minDist = dist;
            }
        }
    }

    return closestPair;
}

double euclideanDistance(const Point& a, const Point& b) {
    double distX = a.x - b.x;
    double distY = a.y - b.y;
    return sqrt(distX * distX + distY * distY);
}

bool sortByY(const Point& a, const Point& b) {
    return a.y < b.y;
}

pair<Point, Point> bruteForce(vector<Point>& points) {
    pair<Point, Point> closestPair(Point{INT_MIN, INT_MIN}, Point{INT_MAX, INT_MAX});
    double minDist = euclideanDistance(closestPair.first, closestPair.second);

    for (int i = 0; i < points.size(); ++i) {
        for (int j = i + 1; j < points.size(); ++j) {
            double dist = euclideanDistance(points[i], points[j]);
            if (dist < minDist) {
                closestPair = {points[i], points[j]};
                minDist = dist;
            }
        }
    }

    return closestPair;
}
