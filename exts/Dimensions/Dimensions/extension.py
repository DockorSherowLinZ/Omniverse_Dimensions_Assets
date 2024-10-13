import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[Dimensions] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class DimensionsExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[Dimensions] Dimensions startup")

        self._count = 0

        self._window = ui.Window("My Window", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")


                def on_click():
                    self._count += 1
                    label.text = f"count: {self._count}"

                def on_reset():
                    self._count = 0
                    label.text = "empty"

                on_reset()

                with ui.HStack():
                    ui.Button("Add", clicked_fn=on_click)
                    ui.Button("Reset", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[Dimensions] Dimensions shutdown")
'''
from pxr import Usd, UsdGeom

# 讀取USD模型文件
stage = Usd.Stage.Open('path_to_your_3d_model_file.usd')

# 假設你的3D物體在根層級
root_prim = stage.GetPseudoRoot()

# 遍歷所有子物件
for prim in root_prim.GetAllChildren():
    if prim.GetTypeName() == 'Mesh':
        bbox = UsdGeom.BBoxCache(Usd.TimeCode.Default(), [UsdGeom.Imageable])
        bounding_box = bbox.ComputeWorldBound(prim).GetRange()
        
        # 計算物體的尺寸
        size = bounding_box.GetSize()
        length, width, height = size[0], size[1], size[2]

        print(f'物體: {prim.GetName()}')
        print(f'長度: {length:.2f}')
        print(f'寬度: {width:.2f}')
        print(f'高度: {height:.2f}')

'''