from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.item.BlockItemModel as _BlockItemModel
_BlockItemModel = _BlockItemModel
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockItemModel():
    """dev.ultreon.quantum.client.model.item.BlockItemModel"""
 
    @staticmethod
    def _wrap(java_value: _BlockItemModel) -> 'BlockItemModel':
        return BlockItemModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockItemModel):
        """
        Dynamic initializer for BlockItemModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockItemModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockItemModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOffset(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.BlockItemModel.getOffset()"""
        return 'math.Vector3'._wrap(super(BlockItemModel, self).getOffset())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.item.BlockItemModel.getModel()"""
        return 'g3d.Model'._wrap(super(BlockItemModel, self).getModel())

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.item.BlockItemModel.resourceId()"""
        return 'util.Identifier'._wrap(super(BlockItemModel, self).resourceId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getScale(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.BlockItemModel.getScale()"""
        return 'math.Vector3'._wrap(super(BlockItemModel, self).getScale())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Supplier'):
        """public dev.ultreon.quantum.client.model.item.BlockItemModel(java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        val = _BlockItemModel(arg0)
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.item.BlockItemModel.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(_BlockItemModel, self).load(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.item.BlockItemModel
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import dev.ultreon.quantum.client.model.item.BlockItemModel as _BlockItemModel
_BlockItemModel = _BlockItemModel
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

import java.lang.String as _String
_String = _String
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BlockItemModel():
    """dev.ultreon.quantum.client.model.item.BlockItemModel"""
 
    @staticmethod
    def _wrap(java_value: _BlockItemModel) -> 'BlockItemModel':
        return BlockItemModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BlockItemModel):
        """
        Dynamic initializer for BlockItemModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BlockItemModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BlockItemModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getOffset(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.BlockItemModel.getOffset()"""
        return 'math.Vector3'._wrap(super(BlockItemModel, self).getOffset())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.item.BlockItemModel.getModel()"""
        return 'g3d.Model'._wrap(super(BlockItemModel, self).getModel())

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.item.BlockItemModel.resourceId()"""
        return 'util.Identifier'._wrap(super(BlockItemModel, self).resourceId())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getScale(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.BlockItemModel.getScale()"""
        return 'math.Vector3'._wrap(super(BlockItemModel, self).getScale())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Supplier'):
        """public dev.ultreon.quantum.client.model.item.BlockItemModel(java.util.function.Supplier<dev.ultreon.quantum.client.model.block.BlockModel>)"""
        val = _BlockItemModel(arg0)
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.item.BlockItemModel.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(_BlockItemModel, self).load(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: dev.ultreon.quantum.client.model.item.BlockItemModel 
 
 
# CLASS: dev.ultreon.quantum.client.model.item.ItemModel
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
import dev.ultreon.quantum.client.resources.LoadableResource as _LoadableResource
_LoadableResource = _LoadableResource
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

from abc import abstractmethod, ABC
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

import dev.ultreon.quantum.client.model.item.ItemModel as _ItemModel
_ItemModel = _ItemModel
 
class ItemModel():
    """dev.ultreon.quantum.client.model.item.ItemModel"""
 
    @staticmethod
    def _wrap(java_value: _ItemModel) -> 'ItemModel':
        return ItemModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemModel):
        """
        Dynamic initializer for ItemModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getScale()"""
        return 'math.Vector3'._wrap(super(ItemModel, self).getScale())

    @abstractmethod
    def resourceId(self, ):
        """public abstract dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.resources.LoadableResource.resourceId()"""
        pass

    @abstractmethod
    def getModel(self, ):
        """public abstract com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.item.ItemModel.getModel()"""
        pass

    @abstractmethod
    def load(self, arg0: 'QuantumClient'):
        """public abstract void dev.ultreon.quantum.client.resources.LoadableResource.load(dev.ultreon.quantum.client.QuantumClient)"""
        pass

    @overload
    def getOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getOffset()"""
        return 'math.Vector3'._wrap(super(ItemModel, self).getOffset()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.item.BakedItemModel
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.item.ItemModel as _ItemModel
_ItemModel = _ItemModel
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.client.model.item.BakedItemModel as _BakedItemModel
_BakedItemModel = _BakedItemModel
import java.lang.Integer as _int
import dev.ultreon.quantum.client.model.BakedModel as _BakedModel
_BakedModel = _BakedModel
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BakedItemModel():
    """dev.ultreon.quantum.client.model.item.BakedItemModel"""
 
    @staticmethod
    def _wrap(java_value: _BakedItemModel) -> 'BakedItemModel':
        return BakedItemModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BakedItemModel):
        """
        Dynamic initializer for BakedItemModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BakedItemModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BakedItemModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSource(self) -> 'ItemModel':
        """public dev.ultreon.quantum.client.model.item.ItemModel dev.ultreon.quantum.client.model.item.BakedItemModel.getSource()"""
        return 'ItemModel'._wrap(super(BakedItemModel, self).getSource())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.BakedModel.getModel()"""
        return 'g3d.Model'._wrap(super(model.BakedModel, self).getModel())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public final dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.BakedModel.resourceId()"""
        return 'util.Identifier'._wrap(super(model.BakedModel, self).resourceId())

    @overload
    def __init__(self, arg0: 'Model', arg1: 'ItemModel'):
        """public dev.ultreon.quantum.client.model.item.BakedItemModel(com.badlogic.gdx.graphics.g3d.Model,dev.ultreon.quantum.client.model.item.ItemModel)"""
        val = _BakedItemModel(arg0, arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.client.model.item.FlatItemModel
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
try:
    from pygdx.graphics import g3d
except ImportError:
    g3d = _import_once("pygdx.graphics.g3d")

import java.lang.Object as _object
from builtins import type
try:
    from pyquantum import client
except ImportError:
    client = _import_once("pyquantum.client")

try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import dev.ultreon.quantum.client.model.item.FlatItemModel as _FlatItemModel
_FlatItemModel = _FlatItemModel
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.client.model.item.ItemModel as _ItemModel
_ItemModel = _ItemModel
import dev.ultreon.quantum.item.Item as _Item
_Item = _Item
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.Model as _Model
_Model = _Model
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FlatItemModel():
    """dev.ultreon.quantum.client.model.item.FlatItemModel"""
 
    @staticmethod
    def _wrap(java_value: _FlatItemModel) -> 'FlatItemModel':
        return FlatItemModel(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FlatItemModel):
        """
        Dynamic initializer for FlatItemModel.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FlatItemModel__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FlatItemModel__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getModel(self) -> 'g3d.Model':
        """public com.badlogic.gdx.graphics.g3d.Model dev.ultreon.quantum.client.model.item.FlatItemModel.getModel()"""
        return 'g3d.Model'._wrap(super(FlatItemModel, self).getModel())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def resourceId(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.client.model.item.FlatItemModel.resourceId()"""
        return 'util.Identifier'._wrap(super(FlatItemModel, self).resourceId())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getScale(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getScale()"""
        return 'math.Vector3'._wrap(super(ItemModel, self).getScale())

    @overload
    def __init__(self, arg0: 'Item'):
        """public dev.ultreon.quantum.client.model.item.FlatItemModel(dev.ultreon.quantum.item.Item)"""
        val = _FlatItemModel(arg0)
        self.__wrapper = val

    @override
    @overload
    def load(self, arg0: 'QuantumClient'):
        """public void dev.ultreon.quantum.client.model.item.FlatItemModel.load(dev.ultreon.quantum.client.QuantumClient)"""
        super(_FlatItemModel, self).load(arg0)

    @overload
    def getItem(self) -> 'item.Item':
        """public dev.ultreon.quantum.item.Item dev.ultreon.quantum.client.model.item.FlatItemModel.getItem()"""
        return 'item.Item'._wrap(super(FlatItemModel, self).getItem())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getOffset(self) -> 'math.Vector3':
        """public default com.badlogic.gdx.math.Vector3 dev.ultreon.quantum.client.model.item.ItemModel.getOffset()"""
        return 'math.Vector3'._wrap(super(ItemModel, self).getOffset())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())