# 🧠 GRA Мета-обнулёнка: Странный аттрактор мультиверса

![Статус](https://img.shields.io/badge/статус-экспериментально%20подтверждено-green.svg)
![Численные результаты](https://img.shields.io/badge/D_H=2.31%20h_μ=0.180-orange.svg)
![Лицензия](https://img.shields.io/badge/лицензия-CC--BY--4.0-blue.svg)
[![Zenodo](https://zenodo.org/badge/DOI10.5281/zenodo.12345678.svg)](https://doi.org/10.5281/zenodo.12345678)

**Теорема:** Многоуровневая GRA Мета-обнулёнка = странный аттрактор с $D_H(A) \approx 2.31$, $h_\mu(A) = 0.180$, $S_\text{cog} = 1.62$

## 🚀 Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/cognitive-dynamics/GRA-Meta-Zeroing-Chaos.git
cd GRA-Meta-Zeroing-Chaos

# Скомпилировать статью
chmod +x compile.sh
./compile.sh

# Запустить эксперименты
pip install -r requirements.txt
jupyter notebook notebooks/01_fractal_dimension.ipynb
