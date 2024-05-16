from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder as _ConeShapeBuilder
_ConeShapeBuilder = _ConeShapeBuilder
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConeShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ConeShapeBuilder) -> 'ConeShapeBuilder':
        return ConeShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConeShapeBuilder):
        """
        Dynamic initializer for ConeShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConeShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConeShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder()"""
        val = _ConeShapeBuilder()
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int)"""
        _ConeShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder()"""
        val = _ConeShapeBuilder()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float)"""
        _ConeShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: bool):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float,boolean)"""
        _ConeShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _boolean.valueOf(arg7))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder as _ConeShapeBuilder
_ConeShapeBuilder = _ConeShapeBuilder
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConeShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ConeShapeBuilder) -> 'ConeShapeBuilder':
        return ConeShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConeShapeBuilder):
        """
        Dynamic initializer for ConeShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConeShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConeShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder()"""
        val = _ConeShapeBuilder()
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int)"""
        _ConeShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder()"""
        val = _ConeShapeBuilder()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float)"""
        _ConeShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: bool):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float,boolean)"""
        _ConeShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _boolean.valueOf(arg7))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ConeShapeBuilder 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder as _BoxShapeBuilder
_BoxShapeBuilder = _BoxShapeBuilder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
try:
    from pygdx.math import collision
except ImportError:
    collision = _import_once("pygdx.math.collision")

import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BoxShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _BoxShapeBuilder) -> 'BoxShapeBuilder':
        return BoxShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BoxShapeBuilder):
        """
        Dynamic initializer for BoxShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BoxShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BoxShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float)"""
        _BoxShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder()"""
        val = _BoxShapeBuilder()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Matrix4'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Matrix4)"""
        _BoxShapeBuilder.build(arg0, arg1)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'BoundingBox'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.collision.BoundingBox)"""
        _BoxShapeBuilder.build(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder()"""
        val = _BoxShapeBuilder()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,float,float)"""
        _BoxShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: 'VertexInfo', arg5: 'VertexInfo', arg6: 'VertexInfo', arg7: 'VertexInfo', arg8: 'VertexInfo'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo)"""
        _BoxShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3', arg8: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BoxShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        _BoxShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder as _CylinderShapeBuilder
_CylinderShapeBuilder = _CylinderShapeBuilder
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CylinderShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _CylinderShapeBuilder) -> 'CylinderShapeBuilder':
        return CylinderShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CylinderShapeBuilder):
        """
        Dynamic initializer for CylinderShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CylinderShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CylinderShapeBuilder__wrapper":
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder()"""
        val = _CylinderShapeBuilder()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float)"""
        _CylinderShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int)"""
        _CylinderShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4))

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
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder()"""
        val = _CylinderShapeBuilder()
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: float, arg6: float, arg7: bool):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CylinderShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,float,float,boolean)"""
        _CylinderShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _boolean.valueOf(arg7))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder as _ArrowShapeBuilder
_ArrowShapeBuilder = _ArrowShapeBuilder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrowShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ArrowShapeBuilder) -> 'ArrowShapeBuilder':
        return ArrowShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrowShapeBuilder):
        """
        Dynamic initializer for ArrowShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrowShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrowShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder()"""
        val = _ArrowShapeBuilder()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,float,float,float,float,int)"""
        _ArrowShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _int.valueOf(arg9))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.ArrowShapeBuilder()"""
        val = _ArrowShapeBuilder()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder as _EllipseShapeBuilder
_EllipseShapeBuilder = _EllipseShapeBuilder
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EllipseShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _EllipseShapeBuilder) -> 'EllipseShapeBuilder':
        return EllipseShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EllipseShapeBuilder):
        """
        Dynamic initializer for EllipseShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EllipseShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EllipseShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: float, arg6: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, _float.valueOf(arg5), _float.valueOf(arg6))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: 'Vector3', arg8: float, arg9: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, arg6, arg7, _float.valueOf(arg8), _float.valueOf(arg9))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, arg17: float, arg18: float, arg19: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15), _float.valueOf(arg16), _float.valueOf(arg17), _float.valueOf(arg18), _float.valueOf(arg19))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3', arg6: float, arg7: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5, _float.valueOf(arg6), _float.valueOf(arg7))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float, arg17: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15), _float.valueOf(arg16), _float.valueOf(arg17))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: 'Vector3', arg7: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), arg6, arg7)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, arg6)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15), _float.valueOf(arg16))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,int,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: 'Vector3', arg5: 'Vector3'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), arg4, arg5)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder()"""
        val = _EllipseShapeBuilder()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder()"""
        val = _EllipseShapeBuilder()
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: 'Vector3', arg7: float, arg8: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), arg3, arg4, arg5, arg6, _float.valueOf(arg7), _float.valueOf(arg8))

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int,float,float,float,float,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: int, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.EllipseShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,int,float,float,float,float,float,float,float,float)"""
        _EllipseShapeBuilder.build(arg0, _float.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder as _BaseShapeBuilder
_BaseShapeBuilder = _BaseShapeBuilder
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class BaseShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _BaseShapeBuilder) -> 'BaseShapeBuilder':
        return BaseShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BaseShapeBuilder):
        """
        Dynamic initializer for BaseShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BaseShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BaseShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder()"""
        val = _BaseShapeBuilder()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.BaseShapeBuilder()"""
        val = _BaseShapeBuilder()
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder as _CapsuleShapeBuilder
_CapsuleShapeBuilder = _CapsuleShapeBuilder
from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CapsuleShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _CapsuleShapeBuilder) -> 'CapsuleShapeBuilder':
        return CapsuleShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CapsuleShapeBuilder):
        """
        Dynamic initializer for CapsuleShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CapsuleShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CapsuleShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,int)"""
        _CapsuleShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _int.valueOf(arg3))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder()"""
        val = _CapsuleShapeBuilder()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.CapsuleShapeBuilder()"""
        val = _CapsuleShapeBuilder()
        self.__wrapper = val

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder
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
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder as _RenderableShapeBuilder
_RenderableShapeBuilder = _RenderableShapeBuilder
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RenderableShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _RenderableShapeBuilder) -> 'RenderableShapeBuilder':
        return RenderableShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RenderableShapeBuilder):
        """
        Dynamic initializer for RenderableShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RenderableShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RenderableShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder()"""
        val = _RenderableShapeBuilder()
        self.__wrapper = val

    @staticmethod
    @overload
    def buildNormals(arg0: 'MeshPartBuilder', arg1: 'RenderableProvider', arg2: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder.buildNormals(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.RenderableProvider,float)"""
        _RenderableShapeBuilder.buildNormals(arg0, arg1, _float.valueOf(arg2))

    @staticmethod
    @overload
    def buildNormals(arg0: 'MeshPartBuilder', arg1: 'RenderableProvider', arg2: float, arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder.buildNormals(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.RenderableProvider,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        _RenderableShapeBuilder.buildNormals(arg0, arg1, _float.valueOf(arg2), arg3, arg4, arg5)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder()"""
        val = _RenderableShapeBuilder()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def buildNormals(arg0: 'MeshPartBuilder', arg1: 'Renderable', arg2: float, arg3: 'Color', arg4: 'Color', arg5: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.RenderableShapeBuilder.buildNormals(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.Renderable,float,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        _RenderableShapeBuilder.buildNormals(arg0, arg1, _float.valueOf(arg2), arg3, arg4, arg5)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder as _FrustumShapeBuilder
_FrustumShapeBuilder = _FrustumShapeBuilder
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FrustumShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _FrustumShapeBuilder) -> 'FrustumShapeBuilder':
        return FrustumShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FrustumShapeBuilder):
        """
        Dynamic initializer for FrustumShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FrustumShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FrustumShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Camera'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.Camera)"""
        _FrustumShapeBuilder.build(arg0, arg1)

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder()"""
        val = _FrustumShapeBuilder()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder()"""
        val = _FrustumShapeBuilder()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Camera', arg2: 'Color', arg3: 'Color', arg4: 'Color', arg5: 'Color', arg6: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.Camera,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        _FrustumShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, arg6)

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Frustum', arg2: 'Color', arg3: 'Color'):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.FrustumShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Frustum,com.badlogic.gdx.graphics.Color,com.badlogic.gdx.graphics.Color)"""
        _FrustumShapeBuilder.build(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder as _PatchShapeBuilder
_PatchShapeBuilder = _PatchShapeBuilder
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PatchShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _PatchShapeBuilder) -> 'PatchShapeBuilder':
        return PatchShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PatchShapeBuilder):
        """
        Dynamic initializer for PatchShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PatchShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PatchShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Vector3', arg2: 'Vector3', arg3: 'Vector3', arg4: 'Vector3', arg5: 'Vector3', arg6: int, arg7: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3,int,int)"""
        _PatchShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, arg5, _int.valueOf(arg6), _int.valueOf(arg7))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder()"""
        val = _PatchShapeBuilder()
        self.__wrapper = val

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'VertexInfo', arg2: 'VertexInfo', arg3: 'VertexInfo', arg4: 'VertexInfo', arg5: int, arg6: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder$VertexInfo,int,int)"""
        _PatchShapeBuilder.build(arg0, arg1, arg2, arg3, arg4, _int.valueOf(arg5), _int.valueOf(arg6))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder()"""
        val = _PatchShapeBuilder()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float, arg9: float, arg10: float, arg11: float, arg12: float, arg13: float, arg14: float, arg15: float, arg16: int, arg17: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.PatchShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,float,float,float,float,float,float,float,float,float,float,float,float,int,int)"""
        _PatchShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _float.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10), _float.valueOf(arg11), _float.valueOf(arg12), _float.valueOf(arg13), _float.valueOf(arg14), _float.valueOf(arg15), _int.valueOf(arg16), _int.valueOf(arg17))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder as _SphereShapeBuilder
_SphereShapeBuilder = _SphereShapeBuilder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

from builtins import bool
try:
    from pygdx.graphics.g3d import utils
except ImportError:
    utils = _import_once("pygdx.graphics.g3d.utils")

import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SphereShapeBuilder():
    """com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _SphereShapeBuilder) -> 'SphereShapeBuilder':
        return SphereShapeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SphereShapeBuilder):
        """
        Dynamic initializer for SphereShapeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SphereShapeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SphereShapeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder()"""
        val = _SphereShapeBuilder()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Matrix4', arg2: float, arg3: float, arg4: float, arg5: int, arg6: int, arg7: float, arg8: float, arg9: float, arg10: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Matrix4,float,float,float,int,int,float,float,float,float)"""
        _SphereShapeBuilder.build(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9), _float.valueOf(arg10))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder()"""
        val = _SphereShapeBuilder()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int, arg6: float, arg7: float, arg8: float, arg9: float):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,int,float,float,float,float)"""
        _SphereShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5), _float.valueOf(arg6), _float.valueOf(arg7), _float.valueOf(arg8), _float.valueOf(arg9))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: float, arg2: float, arg3: float, arg4: int, arg5: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,float,float,float,int,int)"""
        _SphereShapeBuilder.build(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), _int.valueOf(arg4), _int.valueOf(arg5))

    @staticmethod
    @overload
    def build(arg0: 'MeshPartBuilder', arg1: 'Matrix4', arg2: float, arg3: float, arg4: float, arg5: int, arg6: int):
        """public static void com.badlogic.gdx.graphics.g3d.utils.shapebuilders.SphereShapeBuilder.build(com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder,com.badlogic.gdx.math.Matrix4,float,float,float,int,int)"""
        _SphereShapeBuilder.build(arg0, arg1, _float.valueOf(arg2), _float.valueOf(arg3), _float.valueOf(arg4), _int.valueOf(arg5), _int.valueOf(arg6))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())