# blender_exportKeyframesJson

Blenderのキーフレームを取得してjsonでexportするScriptです。  
  
動作確認済み：Blender4.2.1

## How to use

1. `exportKeyframesJson.py`をBlenderの`Text Editor`にコピペ or `Open Text`で読み込みする
2. `exportKeyframesJson()`の引数に取得したいアニメーションのaction名を入れる（現状は選択したオブジェクトのaction名が入るようにしています）
3. `Run Script`ボタンを押してScriptを実行

すると、blendデータの同階層に以下のような`keyframes.json`が出力されます。

```json:keyframes.json
{
  "nodes[\"Mapping\"].inputs[1].default_value_0": {
    "1": 0.0,
    "57": 2.0
  },
  "nodes[\"Mapping\"].inputs[1].default_value_1": {
    "1": 0.0,
    "57": 0.0
  },
  "nodes[\"Mapping\"].inputs[1].default_value_2": {
    "1": 0.0,
    "57": 0.0
  },
  "nodes[\"Mapping\"].inputs[2].default_value_0": {
    "1": 0.0,
    "57": 1.5707963705062866
  },
  "nodes[\"Mapping\"].inputs[2].default_value_1": {
    "1": 0.0,
    "57": 0.0
  },
  "nodes[\"Mapping\"].inputs[2].default_value_2": {
    "1": 0.0,
    "57": 0.0
  }
}
```

第一階層の変数名（`"nodes[\"Mapping\"].inputs[1].default_value_0"`などの部分）はプロパティ（Location、Rotation、Scaleとか）が入っています。
最後の数字はプロパティのインデックスを表していて、以下のようにそれぞれ`x` `y` `z` となっています。

| Index | 座標 |
|:-:|:-:|
| 0 | x |
| 1 | y |
| 2 | z |

第一階層の値のオブジェクト（`{"1": 0.0, "57": 2.0}`などの部分）は変数名の方は`フレーム`、値の方はその`キーフレームの値`が入っています。

アニメーションをbakeしてから実行すれば全ての値が取れます🙆‍♀️