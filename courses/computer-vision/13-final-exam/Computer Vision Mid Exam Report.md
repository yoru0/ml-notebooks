# Computer Vision Mid Exam

**File Soal:** vision-engine-v1.ipynb

**File Jawaban:** vision-engine-v2.ipynb

- **Algorithmic Instability and Theoretical Comprehension**
  - **Identify and explain the mathematical or computational cause of each instability.**
      - Gaussian Smoothing

Kernel yang buggy menghitung ekspresi exp(-(x²+y²)/(2·σ)), bukan 2·σ², sehingga penyebaran Gaussian menggunakan σ (standar deviasi) bukan variance (σ²). Akibatnya, penyebaran menjadi terlalu sempir ketika σ > 1. Selain itu, langkah normalisasi kernel juga tidak ada, menyebabkan jumlah total nilainya tidak sama dengan 1. Ini menyebabkan proses convolution dapat memperkuat atau justru melemahkan intensitas tergantung pada nilai σ dan kernel size. Sehingga perbedaan kecil pada input dapat menghasilkan corner/edge maps yang sangat berbeda.

      - Canny Edge Detection

OpenCV mau input threshold1 < threshold2, tapi code buggy menukar mereka (threshold1=high, threshold2=low), jadi hysteresis menggunakan 150 sebagai “weak” cutoff dan 50 sebagai “strong” cutoff. Ini membuat pixel tidak pernah mencapai lower bound, sehingga tepi lemah tidak bisa terhubung ke tepi kuat. Hal ini menyebabkan ketidakstabilan hasil edge detection.

      - Harris Corner Detection

Nilai Harris direturn tanpa normalization, dan detector menggunakan fixed threshold bernilai 1e7 dan tidak ada non-maximum suppression. Ini menyebabkan corner detection menghasilkan banyak titik palsu (over-response) untuk yang cahaya terang, sebaliknya untuk yang gelap tidak mendeteksi sudut sama sekali.

      - RANSAC Homography

Code buggy mengkonfigurasi homography menggunakan 1-pixel reprojection tolerance dan cuma 100 iterations. Dalam feature matching, hasil deteksi biasanya mengandung banyak outlier. Konfigurasi ini bisa membuat semua pasangan titik dianggap tidak valid. Biasanya RANSAC sebaiknya menggunakan toleransi 3-5 pixel dan iteration antara 1000-2000 kali.

  - **Visualize the impact of incorrect parameters (e.g., corner count, edge noise).**
      - Gaussian Smoothing

![image 1](assets/report-01.png)

![image 2](assets/report-02.png)

Plot 1A/1B – Gaussian Buggy vs Fixed memperlihatkan kernel salah menghasilkan smoothing yang tampak belang. Bagian terang gelap terkompres sehingga noise contrass tinggi tetap muncul, sedangkan untuk versi fixed menampilkan permukaan lebih halus. Ada juga heatmap kernel dalam code menunjukkan jumlah elemen tidak satu sehingga respon intensitas ikut berubah.

      - Canny Edge Detection

![image 3](assets/report-03.png)

![image 4](assets/report-04.png)

1A Canny Edge Counts: 24933 (Buggy) vs 45311 (Fixed)

1B Canny Edge Counts: 346481 (Buggy) vs 19283 (Fixed)

Pada code buggy, menunjukkan edge detection kosong atau hanya memunculkan titik acak karena threshold kuat lemah terbalik. Dibanding dengan versi fixed dimana memunculkan edge memang di tepi objek.

      - Harris Corners

![image 5](assets/report-05.png)

Buggy kpsA: 25 kpsB: 7

Fixed kpsA: 500 kpsB: 500

Gambar 1A – Harris Buggy vs Fixed menggambarkan bahwa buggy menghasilkan sangat sedikit atau tidak ada keypoint pada gambar. Versi fixed dengan normalisasi dan NMS menyebar sudut secara stabil (berwarna merah dot kecil, harus agak di zoom untuk bisa melihat dot merahnya).

      - RANSAC Homography

![image 6](assets/report-06.png)

![image 7](assets/report-07.png)

![image 8](assets/report-08.png)

Diatas ini ada Matches untuk Pair pertama, dimana gambar teratas adalah gambar buggy hampir tidak ada garis hijau yang terlihat yang diakibatkan oleh threshold 1 dan 100 iterasi. Gambar fixed ada 2 karena menggunakan 2 descriptor, yang raw pixel dan HOG dan keduanya memberi Matches yang cukup signifikan.

  - **Propose and implement corrected versions, with quantitative comparison.**
      - Gaussian Smoothing

```python
def gaussian_kernel(size: int, sigma: float) -> np.ndarray:
    """
    Fixed version
    G(x,y) = (1/(2πσ²)) * exp(-(x²+y²)/(2σ²))
    """
    ax = np.arange(-(size//2), size//2 + 1)
    xx, yy = np.meshgrid(ax, ax)

    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    kernel = kernel / np.sum(kernel)

    return kernel.astype(np.float32)
```

Kernel diperbaiki dengan memasukkan varians penuh pada eksponen dan normalisasi ∑K=1.

```text
Quantitative Analysis: Buggy vs Fixed Gaussian Kernel

Kernel size: 7x7, sigma = 2.0

Metric                    Buggy Kernel         Fixed Kernel
-----------------------------------------------------------
Sum (should be 1.0):      12.279130            1.000000
Max value:                1.000000             0.046702
Min value:                0.011109             0.004922
Center value:             1.000000             0.046702
Std deviation:            0.255659             0.011405

Denominator comparison for sigma=2.0:
Buggy: 2 x sigma = 2 x 2.0 = 4.0
Fixed: 2 x sigma² = 2 x 2.0² = 8.0
Ratio: 2.0x difference in spread
```

Perbandingan dan analisis menunjukkan kernel buggy menjumlah 12.279 dB dengan puncak 1.0, sedangkan versi fixed jumlahnya 1.0 dengan puncak 0.0467.

      - Canny Edge Detection

```python
def canny(img: np.ndarray, low: int=50, high: int=150) -> np.ndarray:
    """
    Canny uses double thresholding for hysteresis:
    - Pixels > high_threshold -> strong edges (kept)
    - Pixels > low_threshold -> weak edges (kept only if connected to strong)
    - Pixels < low_threshold -> suppressed
    """
    return cv2.Canny(img, threshold1=low, threshold2=high)
```

Function diperbaiki dengan mengubah threshold1=low dan threshold2=high.

```text
Quantitative Analysis: Buggy vs Fixed Canny Edge Detection

1A Canny Edge Counts: 24933 (Buggy) vs 45311 (Fixed)
1B Canny Edge Counts: 346481 (Buggy) vs 19283 (Fixed)
```

Hitungan edge pixel pada Pair 1A, jumlah edge naik dari 24933 (buggy) menjadi 45311 (fixed) karena tepi penting tidak lagi dipotong; sebaliknya pada B, nilai turun karena noise yang tadinya salah dianggap “strong edge” sekarang tersaring.

      - Harris Corner Detection

```python
def harris_kps(R: np.ndarray, thresh: float=0.01, max_kps: int=500) -> List[cv2.KeyPoint]:
    """
    Harris keypoint extraction with adaptive threshold and non-maximum suppression.
    """
    thresh = thresh * R.max()
    R_thresh = np.zeros_like(R)
    R_thresh[R > thresh] = R[R > thresh]

    R_dilated = cv2.dilate(R_thresh, None)
    local_max = (R_thresh == R_dilated)
    ys, xs = np.where(local_max & (R_thresh > 0))

    strengths = R[ys, xs]
    sorted_idx = np.argsort(-strengths)
    if max_kps is not None:
        sorted_idx = sorted_idx[:max_kps]

    kps = [cv2.KeyPoint(float(xs[i]), float(ys[i]), 3) for i in sorted_idx]
    return kps
```

Untuk function harris_response dinormalisasi ke [0,1], lalu di harris_kps dijadikan adaptif thresh * R.max() dan diikuti non max suppression sebelum dibatasi max 500 keypoints.

```text
Quantitative Analysis: Buggy vs Fixed Harris Corner Detection

Image A Response Statistics:
Buggy (raw):         Min=-7.183029e+07, Max=6.423012e+07, Mean=-1.654253e+04
Fixed (normalized): Min=-0.000000, Max=1.000000, Mean=0.847904

Image B Response Statistics:
Buggy (raw):         Min=-5.187985e+07, Max=2.121732e+07, Mean=-2.182915e+04
Fixed (normalized): Min=-0.000000, Max=1.000000, Mean=0.776632

Corner Detection Results:
Image A: Buggy=25 corners, Fixed=500 corners
Image B: Buggy=7 corners, Fixed=500 corners
```

Hasilnya jauh lebih stabil dan banyak, pair 1 dari 25->500 (gambar A) dan 7->500 (gambar B).

      - RANSAC Homography

```python
def ransac_homography(kps1, kps2, matches, reproj=4.0, maxIters=2000):
    """
    - reproj=4.0 pixels (typical for noisy features)
    - maxIters=2000 (gives high probability of finding good model)
    """
    if len(matches) < 4:
        print("Not enough matches for RANSAC.")
        return None, None

    pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
    pts2 = np.float32([kps2[m.trainIdx].pt for m in matches]).reshape(-1,1,2)
    H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, ransacReprojThreshold=reproj, maxIters=maxIters)
    return H, mask
```

Parameter diperlonggar ke reproj=4 dan maxIters=2000. Hasilnya terlihat pada mask inlier. Untuk Pair-1 hasil buggy gagal total (0/1), sedangkan versi fixed menghasilkan 128/177 inlier dan HOG 138/145; Pair‑2 naik dari 0/4 menjadi 9/91 (patch) dan Pair‑3 dari 0/1 menjadi 17/110 (patch) serta 6/13 (HOG).

  - **Provide theoretical justification for your corrections using equations and short commentary.**
      - Gaussian Smoothing

Rumus gaussian: G(x,y) = exp(-(x²+y²)/(2·σ²)). Faktor σ² di penyebut mengontrol lebar distribusi. Lalu normalisasi memastikan jumlah total adalah 1. Versi buggy menggunakan sigma, bukan sigma^2 serta tanpa normalisasi yang membuat kerjel sensitif tiba tiba kuat dan lemah.

      - Canny

Menggunakan teori T_low < T_high untuk hysteresis.Bila tertukar T_low > T_high, mayoritas pixel salah klasifikasi (week dianggap strong atau sebaliknya), memutus konektivitas dan membuat map jadi tidak konsisten.

      - Harris Corners

Harris response: R = det(M) – k x (trace(M))^2. Nilai R berbanding lurus dengan intensitas dan kontras. Karena itum, menggunakan R >= 10e7 membuat detektor sensitif terhadap lighting. Normalisasi R ke [0,1] dan menerapkan non max suppression memastikan hanya puncak yang diambil, konsisten dengan analisis eigenvalue Harris.

      - RANSAC Homography

Peluang minimal untuk mendapatkan sampel bebas outlier berukuran s=4 dari proporsi inlier p dalam N iterasi adalah (1-(1-p^s)^N). Dengan p=0.3, konfigurasi buggy (N=100) memberi peluang <10%.RANSAC memerlukan iterasi yang banyak ketika outlier tinggi, sehingga maxIter=3000 akan lebih stabil dibanding maxIter=100.

- **Local Feature Descriptor Redesign**
  - **Design and implement an improved classical descriptor (e.g., gradient-based HOG, LBP, or hybrid).**
      - Saya menambakan function extract_hog yang membangun descriptor HOG classic di sekitar setiap keypoint. Implementasinya menggunakan gradien x,y dihitung dengan Sobel, dikonversi ke magnitude dan orientasi 0-180 derajat, lalu setiap patch berukuran 20x20 diberikan bobot Gaussian agar kontribusi pusatnya lebih besar. Patch dibagi ke sel 5x5 pixel dengan histogram 8 bins. Setiap pixel menyalurkan magnitude ke dua bin terdekat menggunakan interpolasi linear. Histogram disatukan per blok 2x2 sel, dinormalisasi L2, dan di concat sehingga setiap keypoint menghasilkan vector 4x4x8x2 = 288.

```python
def extract_hog(img: np.ndarray, kps: List[cv2.KeyPoint], patch: int=20, cell_size: int=5, block_size: int=2, bins: int=8) -> Tuple[np.ndarray, List[int]]:
    """Extract HOG descriptors at keypoint locations"""
    r = patch // 2
    H, W = img.shape[:2]
    n_cells = patch // cell_size

    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
    magnitude, angle = cv2.cartToPolar(gx, gy, angleInDegrees=True)
    angle = angle % 180

    sigma = patch / 2.0
    gaussian_window = cv2.getGaussianKernel(patch, sigma)
    gaussian_weight = gaussian_window @ gaussian_window.T

    descs, keep_idx = [], []

    for i, kp in enumerate(kps):
        x, y = int(round(kp.pt[0])), int(round(kp.pt[1]))
        x0, x1, y0, y1 = x-r, x+r, y-r, y+r

        if x0 < 0 or y0 < 0 or x1 > W or y1 > H:
            continue

        mag_patch = magnitude[y0:y1, x0:x1] * gaussian_weight
        ang_patch = angle[y0:y1, x0:x1]

        cells = np.zeros((n_cells, n_cells, bins), dtype=np.float32)
        bin_width = 180.0 / bins

        for cy in range(n_cells):
            for cx in range(n_cells):
                y_start, y_end = cy*cell_size, (cy+1)*cell_size
                x_start, x_end = cx*cell_size, (cx+1)*cell_size

                cell_mag = mag_patch[y_start:y_end, x_start:x_end]
                cell_ang = ang_patch[y_start:y_end, x_start:x_end]

                hist = np.zeros(bins, dtype=np.float32)
                for m, a in zip(cell_mag.flatten(), cell_ang.flatten()):
                    if m < 1e-5:
                          continue
                    b = int(np.floor(a / bin_width)) % bins
                    hist[b] += m

                cells[cy, cx] = hist

        block_desc = []
        for by in range(n_cells - block_size + 1):
            for bx in range(n_cells - block_size + 1):
                block = cells[by:by+block_size, bx:bx+block_size, :].flatten()

                norm = np.linalg.norm(block)
                if norm > 1e-6:
                    block = block / norm
                    block = np.clip(block, 0, 0.2)
                    norm = np.linalg.norm(block)
                    if norm > 1e-6:
                        block = block / norm

                block_desc.extend(block)

        desc = np.array(block_desc, dtype=np.float32)
        descs.append(desc)
        keep_idx.append(i)

    if len(descs) == 0:
        n_blocks = (n_cells - block_size + 1) ** 2
        desc_dim = n_blocks * (block_size ** 2) * bins
        return np.zeros((0, desc_dim), dtype=np.float32), []

    return np.stack(descs), keep_idx
```

      - Dalam code, descriptor HOG dipakai menggantikan raw patch: D_A_hog, idxA_hog = extract_hog(A1, kpsA) dan D_B_hog, idxB_hog = extract_hog(B1, kpsB)

```python
# Visualization
D_A_hog, idxA_hog = extract_hog(A1, kpsA)
D_B_hog, idxB_hog = extract_hog(B1, kpsB)

print("D_A_hog:", D_A_hog.shape, "D_B_hog:", D_B_hog.shape)
```

```text
D_A_hog: (500, 288) D_B_hog: (500, 288)
```

  - **Explain the theoretical advantage of your descriptor in terms of invariance and distinctiveness.**
      - Block HOG membangun histogram orientasi per sel, lalu dinormalisasi pada blok 2x2. Dua langkah ini memberi invariansi illumination: magnitude gradien (m = sqrt(Ix^2 + Iy^2) menghilangkan offset DC, dan normalisasi L2 pada setiap blok membuat deskriptor skala agnostic terhadap kontras (jika seluruh patch lebih terang, histogram akan dinormalisasi kembali ke panjang 1).
      - Pemetaan sudut 0-180 derajat serta Gaussian weight menambah robustness terhadap rotasi dan jitter posisi. Orientasi 0-180 derajat menyamakan gradien berlawanan arah, sedangkan Gaussian window menekankan pixel dekat pusat keypoint dan menurunkan sensitivitas terhadap translasi kecil.
      - Distinctiveness meningkat karena setiap patch direpresentasikan oleh 4x4 sel x 8 bins x 2 blok sehingga totalnya 288 angka per sudut.
      - Secara teori, seharusnya HOG lebih tidak sensitif terhadap illumination tetapi lumayan ok untuk rotasi / viewpoint.
  - **Test your descriptor using your captured image pairs.**

Test descriptor HOG ada dalam code untuk ketiga pair.

```python
print("Fixed - HOG Descriptors")
H, mask = ransac_homography(kpsA_f_hog, kpsB_f_hog, matchesA_hog, reproj=4.0, maxIters=2000)
print("H:", H is not None, "inliers:", int(mask.sum()) if mask is not None else 0, "/", len(matchesA_hog))

vis_matches_hog = cv2.drawMatches(
    A1, kpsA_f_hog,
    B1, kpsB_f_hog,
    matchesA_hog, None,
    matchColor=[0, 255, 0],
    singlePointColor=[255, 0, 0],
    matchesMask=(mask.ravel().tolist() if mask is not None else None),
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

plt.figure(figsize=(12, 6))
plt.title("Matches (fixed - HOG descriptors)")
plt.imshow(vis_matches_hog)
plt.axis('off')
plt.show()
```

```python
print("\nFixed - HOG Descriptors")

D_A2_hog, idxA2_hog = extract_hog(A2, kpsA2, patch=20, cell_size=5, bins=8)
D_B2_hog, idxB2_hog = extract_hog(B2, kpsB2, patch=20, cell_size=5, bins=8)
print("D_A2_hog:", D_A2_hog.shape, "D_B2_hog:", D_B2_hog.shape)

matchesA2_hog = match_ratio(D_A2_hog, D_B2_hog, ratio=0.75)
print("matches A2 hog:", len(matchesA2_hog))

kpsA2_f_hog = kp_subset(kpsA2, idxA2_hog)
kpsB2_f_hog = kp_subset(kpsB2, idxB2_hog)

H2_hog, mask2_hog = ransac_homography(kpsA2_f_hog, kpsB2_f_hog, matchesA2_hog, reproj=4.0, maxIters=2000)
print("H:", H2_hog is not None, "inliers:", int(mask2_hog.sum()) if mask2_hog is not None else 0, "/", len(matchesA2_hog))

vis_matches2_hog = cv2.drawMatches(
    A2, kpsA2_f_hog,
    B2, kpsB2_f_hog,
    matchesA2_hog, None,
    matchColor=[0, 255, 0],
    singlePointColor=[255, 0, 0],
    matchesMask=(mask2_hog.ravel().tolist() if mask2_hog is not None else None),
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

plt.figure(figsize=(12, 6))
plt.title("Matches 2 (fixed - HOG descriptors)")
plt.imshow(vis_matches2_hog)
plt.axis('off')
plt.show()
```

```python
print("\nFixed - HOG Descriptors")

D_A3_hog, idxA3_hog = extract_hog(A3, kpsA3, patch=20, cell_size=5, bins=8)
D_B3_hog, idxB3_hog = extract_hog(B3, kpsB3, patch=20, cell_size=5, bins=8)
print("D_A3_hog:", D_A3_hog.shape, "D_B3_hog:", D_B3_hog.shape)

matchesA3_hog = match_ratio(D_A3_hog, D_B3_hog, ratio=0.75)
print("matches A3 hog:", len(matchesA3_hog))

kpsA3_f_hog = kp_subset(kpsA3, idxA3_hog)
kpsB3_f_hog = kp_subset(kpsB3, idxB3_hog)

H3_hog, mask3_hog = ransac_homography(kpsA3_f_hog, kpsB3_f_hog, matchesA3_hog, reproj=4.0, maxIters=2000)
print("H:", H3_hog is not None, "inliers:", int(mask3_hog.sum()) if mask3_hog is not None else 0, "/", len(matchesA3_hog))

vis_matches3_hog = cv2.drawMatches(
    A3, kpsA3_f_hog,
    B3, kpsB3_f_hog,
    matchesA3_hog, None,
    matchColor=[0, 255, 0],
    singlePointColor=[255, 0, 0],
    matchesMask=(mask3_hog.ravel().tolist() if mask3_hog is not None else None),
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

plt.figure(figsize=(12, 6))
plt.title("Matches 3 (fixed - HOG descriptors)")
plt.imshow(vis_matches3_hog)
plt.axis('off')
plt.show()
```

  - **Show before–and–after matching visualizations and discuss improvements.**

![image 21](assets/report-21.png)

      - Pair A (illumination) – Panel “Matches (buggy)” hanya berisi garis pendek acak karena cuma ada 1 match dan 0 inlier. Setelah patch descriptor dipakai, visualisasi “Matches (fixed – patch descriptors)” memperlihatkan banyak garis paralel yang konsisten dengan 177 match dan 128 inliers. Versi HOG (“Matches (fixed – HOG descriptors)”) mempertahankan pola garis rapi meski jumlah match lebih sedikit (145 match, 138 inlier) tetapi semua berada di tepi kontras tinggi yang tahan terhadap selisih cahaya.
      - Pair B (perubahan viewpoint) – Visual  matches 2 buggy kosong karena hanya 4 match raw patch buggy dan tidak ada inlier sehingga homografi gagal. Matched 2 fixed – Patch descriptors menampilkan beberapa garis yang mengukuti benda dengan 91 match dan 9 inliers. HOG pada pair ini tidak menemukan cukup pasangan (1 match, 0 inlier) karena sudut pandang berubah terlalu ekstrim sehingga visual tetap kosong.

![image 22](assets/report-22.png)

      - Pair C (jarak / skala) – Match 3 buggy tidak ada garis (1 match, 0 inlier). Matches 3 fixed – patch descriptors terdapat garis hijau dengan 110 match dan 17 inliers. Panel HOG menampilkan  13 match dan 6 inliers.

![image 23](assets/report-23.png)

      - Secara keseluruhan, “Matches … (buggy)” vs “Matches … (fixed …)” memperlihatkan transformasi paling jelas: dari layar yang kosong menjadi bergaris hijau menandakan hubungan konsisten.
- **Image Correspondence and Recognition Application**
  - **Compute image correspondences between your captured image pairs using your improved system.**

Jawaban dan code semua ada di vision-engine-v2.ipynb

```text
Keypoint A1: 500
Keypoint A2: 500
Keypoint B1: 500
Keypoint B2: 500
Keypoint C1: 500
Keypoint C2: 500

Matches Patch Descriptors):
matches A patch: 177
matches B patch: 91
matches C patch: 110

Descriptor shapes (Patch):
D_A1_patch: (500, 121)
D_A2_patch: (500, 121)
D_B1_patch: (500, 121)
D_B2_patch: (500, 121)
D_C1_patch: (500, 121)
D_C2_patch: (500, 121)
```

![image 25](assets/report-25.png)

![image 26](assets/report-26.png)

![image 27](assets/report-27.png)

  - **Apply RANSAC-based geometric verification to refine matches.**

![image 28](assets/report-28.png)

![image 29](assets/report-29.png)

![image 30](assets/report-30.png)

  - **Measure:**
    - **Number of matched inliers,**
    - **Average reprojection error,**
    - **Recognition success (e.g., correctly identifying the same scene).**

```text
           Image Pair         Variation Type  Total Keypoints (Img1)  Total Keypoints (Img2)  Initial Matches  RANSAC Inliers  Inlier Ratio (%)  Avg Reprojection Error (px)  Recognition Success
Pair A (Illumination)        Lighting change                     500                     500              177             128             72.32                     122.9605                  YES
   Pair B (Viewpoint)     Camera angle shift                     500                     500               91               9              9.89                     833.3955                   NO
       Pair C (Scale)  Distance/Scale change                     500                     500              110              17             15.45                     267.1783                  YES

Pair A (Illumination):
  • Number of matched inliers: 128
  • Average reprojection error: 122.9605 pixels
  • Inlier ratio: 72.32%
  • Recognition success: YES - Scene correctly identified

Pair B (Viewpoint):
  • Number of matched inliers: 9
  • Average reprojection error: 833.3955 pixels
  • Inlier ratio: 9.89%
  • Recognition success: NO - Insufficient inliers

Pair C (Scale):
  • Number of matched inliers: 17
  • Average reprojection error: 267.1783 pixels
  • Inlier ratio: 15.45%
  • Recognition success: YES - Scene correctly identified
```

  - **Reflect on how your final pipeline demonstrates robustness to real-world variation (lighting, scale, angle).**
      - Robustness terhadap pencahayaan (Pair A)

Deskriptor yang telah diperbaiki menggunakan normalisasi (x – mean) / std, sehingga tahan terhadap perubahan pencahayaan aditif (pergeseran intensitas) maupun multiplikatif (perubahan kontras).

Hasil: 128/177 inlier (rasio inlier 72,3%)

Reprojection error: 122,9605 px

Pipeline berhasil menangani variasi pencahayaan karena:

- Deskriptor ternormalisasi bersifat invarian terhadap perubahan linear pada kecerahan dan kontras.
- Detektor sudut Harris mendeteksi fitur struktural yang tetap stabil meskipun intensitas berubah.
- RANSAC menyaring outlier yang disebabkan oleh efek pencahayaan non-linear.
      - Robustness terhadap perubahan sudut (Pair B)

Detektor sudut Harris berbasis gradien intensitas di berbagai arah, membuatnya relatif invarian terhadap rotasi kecil hingga sedang.

Hasil: 9/91 inlier (rasio inlier 9,9%)

Reprojection error: 833,3955 px

Pipeline mampu menangani perubahan sudut pandang karena:

- Titik sudut adalah fitur geometrik yang tetap terlihat dari berbagai sudut.
- Model homografi mampu merepresentasikan transformasi perspektif.
- RANSAC dengan 2000 iterasi meningkatkan peluang menemukan model yang benar.
      - Robustness terhadap perubahan skala (Pair C)

Meskipun deskriptor yang digunakan belum sepenuhnya invarian terhadap skala (tidak seperti SIFT), kombinasi antara normalized patch dan RANSAC memberikan ketahanan sebagian.

Hasil: 17/110 inlier (rasio inlier 15,5%)

Reprojection error: 267,1783 piksel

Pipeline menunjukkan toleransi terhadap skala karena:

- Normalisasi memberikan invarian parsial terhadap skala.
- Titik sudut Harris pada berbagai skala sering muncul di lokasi yang berdekatan.
- RANSAC efektif dalam menyaring ketidaksesuaian akibat perbedaan skala.

Buggy System → Fixed System:

- Gaussian kernel: tidak ternormalisasi → dinormalisasi (jumlah elemen = 1.0)
- Canny edges: urutan ambang terbalik → urutan benar (low < high)
- Harris response: nilai mentah → dinormalisasi ke [0,1] dengan non-maximum suppression
- Deskriptor: normalisasi maksimum → normalisasi rata-rata dan standar deviasi (lebih tahan pencahayaan)
- RANSAC: reproj=1.0, iter=100 → reproj=4.0, iter=2000 (lebih kuat terhadap outlier)

Aplikasi Dunia Nyata:

Pipeline ini cocok untuk:

- Image stitching (pembuatan panorama)
- Pengenalan objek di kondisi lingkungan yang bervariasi
- Estimasi posisi dan orientasi kamera
- Pelacakan penanda dalam augmented reality
- Rekonstruksi 3D dari beberapa sudut pandang

Keterbatasan:

- Perubahan skala besar (>3×) dapat gagal tanpa deteksi multi-skala
- Rotasi ekstrem (>45°) menurunkan jumlah kecocokan
- Pencahayaan ekstrem (bayangan keras, sorotan tinggi) dapat menyebabkan kegagalan
- Citra dengan motion blur atau tekstur rendah sulit diproses
- **Comparative Experiment**

  - **Run a controlled comparison between two different descriptors (e.g., your design vs. HOG/LBP). Present a short table of quantitative results and your interpretation.**

Patch vs Hog Descriptors

| Pair | Matches | Inliers | Ratio (%) | Reproj Error px |
|---|---|---|---|---|
| Pair A Patch | 177 | 128 | 72.3 | 122.96 |
| Pair A HOG | 145 | 138 | 95.2 | 14.19 |
| Pair B Patch | 91 | 9 | 9.9 | 833.40 |
| Pair B HOG | 1 | 0 | 0.0 | N/A |
| Pair C Patch | 110 | 17 | 15.5 | 267.18 |
| Pair C HOG | 13 | 6 | 46.2 | 190/59 |

Patch (mean-std) -> simple, cepat, bagus untuk illumination change.

HOG -> lebih bagus untuk geometric precision meskipun lebih lambat
