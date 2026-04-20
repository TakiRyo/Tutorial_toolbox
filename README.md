# Universal AI ToolBox

Python + Streamlitで作る多機能Webアプリの共同開発プロジェクトです。`tools/` 配下に機能を追加するだけで、アプリのメニューに自動で増えていく構成にしています。

## 概要
- フレームワーク: Streamlit
- 対象Python: 3.10以上
- 目的: みんなで1つのWebアプリを作り上げる

## ディレクトリ構成
```
ai-toolbox/
├── app.py              # メインプログラム
├── requirements.txt    # 必要なライブラリ一覧
├── utils/              # 共通関数など
└── tools/              # ← 学生の作業場所
		├── config.py       # 各機能の登録用ファイル
		├── tool_a.py       # 例: おみくじ
		└── tool_b.py       # 例: 画像フィルター
```

## 環境構築（conda推奨）
```
conda create -n ai-toolbox python=3.10
conda activate ai-toolbox
pip install -r requirements.txt
```

### 依存関係のエラーが出た場合
`rembg` の依存で `numba/llvmlite` のビルドに失敗することがあります。以下を先に実行してから `pip install -r requirements.txt` を行ってください。
```
conda install -c conda-forge llvmlite numba
```

## 実行方法
```
streamlit run app.py
```
起動後、ブラウザで `http://localhost:8501` を開きます。

## 停止方法（重要）
Streamlitはファイル監視のために子プロセスが残ることがあります。
1. ターミナルにフォーカスして **Ctrl+C を2回**
2. それでも止まらない場合は以下でPIDを確認して終了
```
lsof -i :8501
kill -9 <PID>
```

## 機能追加の手順
1. `tools/` に自分の機能ファイルを作成（例: `image_filter.py`）
2. そのファイル内に `show()` 関数を定義
3. `tools/config.py` の `TOOLS` に `{ "name": "表示名", "module": "ファイル名(拡張子なし)" }` を追加

### 画面の共通ルール
- サイドバーで切り替えられるUIにする
- 各ページ冒頭に以下を必ず表示
	- `# ## 機能名`
	- `作った人: 名前`

## READMEの更新ルール（新機能を追加したら）
以下のテンプレをREADME末尾の「機能一覧」に追記してください。

**テンプレ:**
```
- 機能名: <表示名>
	- ファイル: tools/<module>.py
	- 概要: <何ができるか>
	- 作成者: <名前>
```

## 共同開発ルール
- まずIssueを作成（機能名・目的・概要）
- ブランチ作成（例: `feature/my-tool`）
- 実装・動作確認
- PRを作成してレビュー依頼
- マージ後にREADMEの機能一覧を更新

## 機能一覧
- 機能名: おみくじ・占い
	- ファイル: tools/tool_a.py
	- 概要: ボタンで運勢とラッキーアイテムを表示
	- 作成者: taki

- 機能名: 画像背景除去・フィルター
	- ファイル: tools/tool_b.py
	- 概要: グレースケール/左右反転の簡易フィルター
	- 作成者: taki

