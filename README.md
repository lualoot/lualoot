<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:161b22,100:1f6feb&height=230&section=header&text=LuaLoot&fontSize=72&fontColor=e6edf3&fontAlignY=38&animation=fadeIn&desc=Lua%20Scripts%20%E2%80%A2%20SA-MP%20%E2%80%A2%20MoonLoader&descSize=18&descColor=8b949e&descAlignY=62" width="100%" alt="LuaLoot header" />

<a href="https://github.com/lualoot">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3000&pause=1000&color=58A6FF&center=true&vCenter=true&width=640&lines=Crafting+clean+Lua+scripts+for+SA-MP;Performance-first.+Lightweight.+Reliable.;Open+source+tools+for+the+SA-MP+community" alt="Typing SVG" />
</a>

<br/>

![Profile Views](https://komarev.com/ghpvc/?username=lualoot&label=Profile+Views&color=1f6feb&style=for-the-badge&labelColor=0d1117)
![Followers](https://img.shields.io/github/followers/lualoot?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117&color=1f6feb)
![Stars](https://img.shields.io/github/stars/lualoot?style=for-the-badge&logo=github&logoColor=white&labelColor=0d1117&color=1f6feb)

</div>

<br/>

## ▍ Tentang LuaLoot

```lua
local LuaLoot = {
    focus    = "Lua scripting untuk SA-MP",
    platform = { "MoonLoader", "SAMP.Lua", "mimgui / ImGui" },
    values   = { "clean code", "performa ringan", "mudah dikustomisasi" },
    status   = "Aktif membangun & merilis script baru",
}
```

LuaLoot adalah tempat kumpulan **script Lua untuk SA-MP (San Andreas Multiplayer)** — mulai dari utilitas client-side, tools produktivitas, hingga antarmuka modern berbasis ImGui. Setiap proyek dibuat dengan fokus pada **kode yang rapi, stabil, dan mudah dipahami**.

<br/>

## ▍ Fokus Pengembangan

<table>
  <tr>
    <td width="50%" valign="top">

### 🧩 Script & Utilitas
- Script MoonLoader siap pakai
- Command & automation client-side
- Helper untuk event & packet SA-MP

    </td>
    <td width="50%" valign="top">

### 🎨 Antarmuka (UI)
- Menu & overlay berbasis **mimgui / ImGui**
- Tema gelap yang konsisten
- Pengaturan tersimpan lewat file config

    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">

### ⚙️ Optimasi
- Penggunaan CPU & memori seminimal mungkin
- Struktur modular dan mudah dirawat
- Penanganan error yang aman

    </td>
    <td width="50%" valign="top">

### 📚 Dokumentasi
- README jelas di setiap repositori
- Contoh penggunaan & changelog
- Panduan instalasi langkah demi langkah

    </td>
  </tr>
</table>

<br/>

## ▍ Tech Stack

<div align="center">

![Lua](https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white)
![MoonLoader](https://img.shields.io/badge/MoonLoader-0d1117?style=for-the-badge&logo=lua&logoColor=58a6ff)
![SAMP.Lua](https://img.shields.io/badge/SAMP.Lua-0d1117?style=for-the-badge&logoColor=white&color=161b22)
![ImGui](https://img.shields.io/badge/mimgui%20%2F%20ImGui-0d1117?style=for-the-badge&logoColor=white&color=161b22)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

</div>

<br/>

## ▍ Contoh Kode

Gaya penulisan yang saya gunakan — ringkas, terstruktur, dan aman:

```lua
script_name("LuaLoot Example")
script_author("LuaLoot")
script_version("1.0.0")

require "lib.moonloader"
local sampev = require "lib.samp.events"

local PREFIX = "{58A6FF}[LuaLoot]{FFFFFF} "

function main()
    while not isSampAvailable() do wait(100) end

    sampRegisterChatCommand("hello", function()
        sampAddChatMessage(PREFIX .. "Script berhasil dimuat!", -1)
    end)

    wait(-1)
end

function sampev.onServerMessage(color, text)
    -- tangani pesan server di sini
end
```

<br/>

## ▍ Proyek Unggulan

<!--START_SECTION:repos-->
> 🚧 **Belum ada proyek publik.** Script Lua SA-MP pertama akan segera hadir — pantau terus!
<!--END_SECTION:repos-->

<br/>

## ▍ Statistik GitHub

<div align="center">

<img src="https://streak-stats.demolab.com?user=lualoot&theme=tokyonight&background=0d1117&border=30363d&ring=1f6feb&fire=58a6ff&currStreakLabel=58a6ff&hide_border=false" alt="GitHub Streak" />

</div>

<!--START_SECTION:stats-->
> 📊 **Belum ada data statistik.** Akan muncul otomatis setelah repositori publik pertama dibuat.
<!--END_SECTION:stats-->

<br/>

## ▍ Struktur Repositori

Setiap proyek mengikuti struktur yang konsisten:

```text
nama-proyek/
├── moonloader/
│   ├── nama_script.lua      # script utama
│   └── config/              # file konfigurasi
├── lib/                     # dependensi (jika ada)
├── README.md                # dokumentasi
├── CHANGELOG.md             # riwayat versi
└── LICENSE
```

<br/>

## ▍ Instalasi Singkat

1. Pastikan **SA-MP** dan **MoonLoader** sudah terpasang.
2. Unduh script dari tab **Releases** atau **Code → Download ZIP**.
3. Salin file `.lua` ke folder `moonloader/` di direktori GTA San Andreas.
4. Jalankan game, lalu masuk ke server SA-MP.

<br/>

## ▍ Kontribusi

Kontribusi, saran, dan laporan bug sangat diterima.

- 🐞 Temukan bug → buka **[Issues](https://github.com/lualoot?tab=repositories)**
- 🔧 Punya perbaikan → kirim **Pull Request**
- ⭐ Suka dengan proyeknya → berikan **Star** pada repositori

<br/>

## ▍ Hubungi Saya

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-lualoot-0d1117?style=for-the-badge&logo=github&logoColor=white)](https://github.com/lualoot)
[![Email](https://img.shields.io/badge/Email-EMAIL-0d1117?style=for-the-badge&logo=gmail&logoColor=58a6ff)](mailto:anonymous.my.id@gmail.com)

</div>

<br/>

<div align="center">

<sub>Dibuat dengan 🖤 untuk komunitas SA-MP</sub>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,50:161b22,100:0d1117&height=120&section=footer" width="100%" alt="footer" />

</div>
