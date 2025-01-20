#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <iomanip> // For formatting

int main() {
    std::ifstream inputFile("./LM_Channel_0180_mean_prof.dat.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Unable to open file." << std::endl;
        return 1;
    }

    std::ofstream outputFile("./output/LM_Channel_180_mean_prof_add_udelta_wdelta.txt");
    if (!outputFile.is_open()) {
        std::cerr << "Unable to open output file." << std::endl;
        return 1;
    }

    std::string line;
    std::vector<std::string> lines;
    int startLine = 72;

    // パラメータを格納する変数
    int nx = 0, ny = 0, nz = 0;
    double u_tau = 0.0, Re_tau = 0.0;

    // ファイル全体を読み込む
    while (std::getline(inputFile, line)) {
        lines.push_back(line);
        // 必要なパラメータを抽出
        if (line.find("Grid (streamwise)       nx") != std::string::npos) {
            nx = std::stoi(line.substr(line.find('=') + 1));
        } else if (line.find("Grid (wall-normal)      ny") != std::string::npos) {
            ny = std::stoi(line.substr(line.find('=') + 1));
        } else if (line.find("Grid (spanwise)         nz") != std::string::npos) {
            nz = std::stoi(line.substr(line.find('=') + 1));
        } else if (line.find("Friction vel         u_tau") != std::string::npos) {
            u_tau = std::stod(line.substr(line.find('=') + 1));
        } else if (line.find("Re_tau              Re_tau") != std::string::npos) {
            Re_tau = std::stod(line.substr(line.find('=') + 1));
        }
    }
    inputFile.close();

    // パラメータの確認
    std::cout << "nx = " << nx << ", ny = " << ny << ", nz = " << nz << ", u_tau = " << u_tau << ", Re_tau = " << Re_tau << std::endl;

    // ヘッダー部分の出力
    for (int i = 0; i < startLine - 2; ++i) {
        outputFile << lines[i] << std::endl;
    }

    // ヘッダーの列名を修正して出力
    outputFile << lines[startLine - 2] << std::setw(24) << "u = U*u_tau" <<  std::setw(24)  << "w = W*u_tau"<< std::endl;
    outputFile << lines[startLine-1] << std::endl;  // データの区切り行を出力

    // データ部分の処理
    for (int i = startLine; i < lines.size(); ++i) {
        std::istringstream iss(lines[i]);
        double y_delta, y_plus, U, dU_dy, W, P;

        // 各列のデータを抽出
        iss >> y_delta >> y_plus >> U >> dU_dy >> W >> P;
         //  U/delta の計算
        double  udelta =  U * u_tau;
        double  wdelta =  W * u_tau;
        // 新しい行を出力 (元の行 + 新しいU列)
        outputFile << std::setw(24) << y_delta
                   << std::setw(24) << y_plus
                   << std::setw(24) << U
                   << std::setw(24) << dU_dy
                   << std::setw(24) << W
                   << std::setw(24) << P
                   << std::setw(24) << udelta
                   << std::setw(24) << wdelta << std::endl;
    }

    outputFile.close();
    std::cout << "File processed successfully. Output saved to" + outputFile << std::endl;

    return 0;
}
