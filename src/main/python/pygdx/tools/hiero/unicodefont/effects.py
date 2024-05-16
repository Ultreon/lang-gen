from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import java.awt.Graphics2D as Graphics2D
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect as _ConfigurableEffect
_ConfigurableEffect = _ConfigurableEffect
import com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect as _Effect
_Effect = _Effect
import java.awt.image.BufferedImage as BufferedImage
from abc import abstractmethod, ABC
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.util.List as List
 
class ConfigurableEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect"""
 
    @staticmethod
    def _wrap(java_value: _ConfigurableEffect) -> 'ConfigurableEffect':
        return ConfigurableEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConfigurableEffect):
        """
        Dynamic initializer for ConfigurableEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConfigurableEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConfigurableEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setValues(self, arg0: 'List'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.setValues(java.util.List)"""
        pass

    @abstractmethod
    def getValues(self, ):
        """public abstract java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.getValues()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect
from pyquantum_helper import import_once as _import_once
import java.awt.Graphics2D as Graphics2D
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect as _ConfigurableEffect
_ConfigurableEffect = _ConfigurableEffect
import com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect as _Effect
_Effect = _Effect
import java.awt.image.BufferedImage as BufferedImage
from abc import abstractmethod, ABC
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.util.List as List
 
class ConfigurableEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect"""
 
    @staticmethod
    def _wrap(java_value: _ConfigurableEffect) -> 'ConfigurableEffect':
        return ConfigurableEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConfigurableEffect):
        """
        Dynamic initializer for ConfigurableEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConfigurableEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConfigurableEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def setValues(self, arg0: 'List'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.setValues(java.util.List)"""
        pass

    @abstractmethod
    def getValues(self, ):
        """public abstract java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.getValues()"""
        pass

    @abstractmethod
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect as _ColorEffect
_ColorEffect = _ColorEffect
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.awt.Graphics2D as Graphics2D
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ColorEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect"""
 
    @staticmethod
    def _wrap(java_value: _ColorEffect) -> 'ColorEffect':
        return ColorEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ColorEffect):
        """
        Dynamic initializer for ColorEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ColorEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ColorEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect()"""
        val = _ColorEffect()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect(java.awt.Color)"""
        val = _ColorEffect(arg0)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.toString()"""
        return str._wrap(super(ColorEffect, self).toString())

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.getColor()"""
        return 'Color'._wrap(super(ColorEffect, self).getColor())

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.setValues(java.util.List)"""
        super(_ColorEffect, self).setValues(arg0)

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
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.setColor(java.awt.Color)"""
        super(_ColorEffect, self).setColor(arg0)

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.getValues()"""
        return 'List'._wrap(super(ColorEffect, self).getValues())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_ColorEffect, self).draw(arg0, arg1, arg2, arg3)

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ColorEffect()"""
        val = _ColorEffect()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil as _EffectUtil
_EffectUtil = _EffectUtil
import java.lang.Object as _object
from builtins import type
import java.awt.image.BufferedImage as _BufferedImage
_BufferedImage = _BufferedImage
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect as _ConfigurableEffect_Value
_Value = _ConfigurableEffect_Value.Value
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EffectUtil():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil"""
 
    @staticmethod
    def _wrap(java_value: _EffectUtil) -> 'EffectUtil':
        return EffectUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EffectUtil):
        """
        Dynamic initializer for EffectUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EffectUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EffectUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def fromString(arg0: str) -> 'Color':
        """public static java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.fromString(java.lang.String)"""
        return Color._wrap(_EffectUtil.fromString(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def intValue(arg0: str, arg1: int, arg2: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.intValue(java.lang.String,int,java.lang.String)"""
        return Value._wrap(_EffectUtil.intValue(arg0, _int.valueOf(arg1), arg2))

    @staticmethod
    @overload
    def optionValue(arg0: str, arg1: str, arg2: 'String', arg3: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.optionValue(java.lang.String,java.lang.String,java.lang.String[][],java.lang.String)"""
        return Value._wrap(_EffectUtil.optionValue(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def colorValue(arg0: str, arg1: 'Color') -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.colorValue(java.lang.String,java.awt.Color)"""
        return Value._wrap(_EffectUtil.colorValue(arg0, arg1))

    @staticmethod
    @overload
    def floatValue(arg0: str, arg1: float, arg2: float, arg3: float, arg4: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.floatValue(java.lang.String,float,float,float,java.lang.String)"""
        return Value._wrap(_EffectUtil.floatValue(arg0, _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3), arg4))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getScratchImage() -> 'BufferedImage':
        """public static java.awt.image.BufferedImage com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.getScratchImage()"""
        return BufferedImage._wrap(_EffectUtil.getScratchImage())

    @staticmethod
    @overload
    def booleanValue(arg0: str, arg1: bool, arg2: str) -> 'Value':
        """public static com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.booleanValue(java.lang.String,boolean,java.lang.String)"""
        return Value._wrap(_EffectUtil.booleanValue(arg0, _boolean.valueOf(arg1), arg2))

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
    def toString(arg0: 'Color') -> str:
        """public static java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil.toString(java.awt.Color)"""
        return str._wrap(_EffectUtil.toString(arg0))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil()"""
        val = _EffectUtil()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.EffectUtil()"""
        val = _EffectUtil()
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.awt.Stroke as Stroke
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect as _OutlineEffect
_OutlineEffect = _OutlineEffect
import java.awt.Graphics2D as Graphics2D
import java.awt.Stroke as _Stroke
_Stroke = _Stroke
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OutlineEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect"""
 
    @staticmethod
    def _wrap(java_value: _OutlineEffect) -> 'OutlineEffect':
        return OutlineEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OutlineEffect):
        """
        Dynamic initializer for OutlineEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OutlineEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OutlineEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getColor()"""
        return 'Color'._wrap(super(OutlineEffect, self).getColor())

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getValues()"""
        return 'List'._wrap(super(OutlineEffect, self).getValues())

    @overload
    def setStroke(self, arg0: 'Stroke'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setStroke(java.awt.Stroke)"""
        super(_OutlineEffect, self).setStroke(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect()"""
        val = _OutlineEffect()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect()"""
        val = _OutlineEffect()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setColor(java.awt.Color)"""
        super(_OutlineEffect, self).setColor(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.toString()"""
        return str._wrap(super(OutlineEffect, self).toString())

    @overload
    def setJoin(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setJoin(int)"""
        super(_OutlineEffect, self).setJoin(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getWidth()"""
        return float._wrap(super(OutlineEffect, self).getWidth())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect(int,java.awt.Color)"""
        val = _OutlineEffect(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_OutlineEffect, self).draw(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getJoin(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getJoin()"""
        return int._wrap(super(OutlineEffect, self).getJoin())

    @overload
    def setWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setWidth(int)"""
        super(_OutlineEffect, self).setWidth(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getStroke(self) -> 'Stroke':
        """public java.awt.Stroke com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getStroke()"""
        return 'Stroke'._wrap(super(OutlineEffect, self).getStroke())

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setValues(java.util.List)"""
        super(_OutlineEffect, self).setValues(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect as _OutlineZigzagEffect
_OutlineZigzagEffect = _OutlineZigzagEffect
from builtins import str
import java.awt.Stroke as Stroke
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect as _OutlineEffect
_OutlineEffect = _OutlineEffect
import java.awt.Graphics2D as Graphics2D
import java.awt.Stroke as _Stroke
_Stroke = _Stroke
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OutlineZigzagEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect"""
 
    @staticmethod
    def _wrap(java_value: _OutlineZigzagEffect) -> 'OutlineZigzagEffect':
        return OutlineZigzagEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OutlineZigzagEffect):
        """
        Dynamic initializer for OutlineZigzagEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OutlineZigzagEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OutlineZigzagEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setWidth(int)"""
        super(_OutlineEffect, self).setWidth(_int.valueOf(arg0))

    @override
    @overload
    def getStroke(self) -> 'Stroke':
        """public java.awt.Stroke com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getStroke()"""
        return 'Stroke'._wrap(super(OutlineEffect, self).getStroke())

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getColor()"""
        return 'Color'._wrap(super(OutlineEffect, self).getColor())

    @override
    @overload
    def getJoin(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getJoin()"""
        return int._wrap(super(OutlineEffect, self).getJoin())

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
    def setJoin(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setJoin(int)"""
        super(_OutlineEffect, self).setJoin(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect(int,java.awt.Color)"""
        val = _OutlineZigzagEffect(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect.toString()"""
        return str._wrap(super(OutlineZigzagEffect, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect()"""
        val = _OutlineZigzagEffect()
        self.__wrapper = val

    @override
    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getWidth()"""
        return float._wrap(super(OutlineEffect, self).getWidth())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_OutlineEffect, self).draw(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect()"""
        val = _OutlineZigzagEffect()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStroke(self, arg0: 'Stroke'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setStroke(java.awt.Stroke)"""
        super(_OutlineEffect, self).setStroke(arg0)

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect.setValues(java.util.List)"""
        super(_OutlineZigzagEffect, self).setValues(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setColor(java.awt.Color)"""
        super(_OutlineEffect, self).setColor(arg0)

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineZigzagEffect.getValues()"""
        return 'List'._wrap(super(OutlineZigzagEffect, self).getValues())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect as _ShadowEffect
_ShadowEffect = _ShadowEffect
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.lang.Float as _float
import java.awt.Graphics2D as Graphics2D
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ShadowEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect"""
 
    @staticmethod
    def _wrap(java_value: _ShadowEffect) -> 'ShadowEffect':
        return ShadowEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShadowEffect):
        """
        Dynamic initializer for ShadowEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShadowEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShadowEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setBlurKernelSize(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setBlurKernelSize(int)"""
        super(_ShadowEffect, self).setBlurKernelSize(_int.valueOf(arg0))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setColor(java.awt.Color)"""
        super(_ShadowEffect, self).setColor(arg0)

    @overload
    def getBlurKernelSize(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getBlurKernelSize()"""
        return int._wrap(super(ShadowEffect, self).getBlurKernelSize())

    @overload
    def getOpacity(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getOpacity()"""
        return float._wrap(super(ShadowEffect, self).getOpacity())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getBlurPasses(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getBlurPasses()"""
        return int._wrap(super(ShadowEffect, self).getBlurPasses())

    @overload
    def setXDistance(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setXDistance(float)"""
        super(_ShadowEffect, self).setXDistance(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect()"""
        val = _ShadowEffect()
        self.__wrapper = val

    @overload
    def getYDistance(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getYDistance()"""
        return float._wrap(super(ShadowEffect, self).getYDistance())

    @overload
    def setYDistance(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setYDistance(float)"""
        super(_ShadowEffect, self).setYDistance(_float.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setValues(java.util.List)"""
        super(_ShadowEffect, self).setValues(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setOpacity(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setOpacity(float)"""
        super(_ShadowEffect, self).setOpacity(_float.valueOf(arg0))

    @overload
    def setBlurPasses(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.setBlurPasses(int)"""
        super(_ShadowEffect, self).setBlurPasses(_int.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getXDistance(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getXDistance()"""
        return float._wrap(super(ShadowEffect, self).getXDistance())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect()"""
        val = _ShadowEffect()
        self.__wrapper = val

    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getColor()"""
        return 'Color'._wrap(super(ShadowEffect, self).getColor())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_ShadowEffect, self).draw(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.getValues()"""
        return 'List'._wrap(super(ShadowEffect, self).getValues())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Color', arg1: int, arg2: int, arg3: float):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect(java.awt.Color,int,int,float)"""
        val = _ShadowEffect(arg0, _int.valueOf(arg1), _int.valueOf(arg2), _float.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ShadowEffect.toString()"""
        return str._wrap(super(ShadowEffect, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
import java.awt.Stroke as Stroke
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect as _OutlineEffect
_OutlineEffect = _OutlineEffect
import java.awt.Graphics2D as Graphics2D
import java.awt.Stroke as _Stroke
_Stroke = _Stroke
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
import com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect as _OutlineWobbleEffect
_OutlineWobbleEffect = _OutlineWobbleEffect
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OutlineWobbleEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect"""
 
    @staticmethod
    def _wrap(java_value: _OutlineWobbleEffect) -> 'OutlineWobbleEffect':
        return OutlineWobbleEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OutlineWobbleEffect):
        """
        Dynamic initializer for OutlineWobbleEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OutlineWobbleEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OutlineWobbleEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setWidth(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setWidth(int)"""
        super(_OutlineEffect, self).setWidth(_int.valueOf(arg0))

    @overload
    def __init__(self, arg0: int, arg1: 'Color'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect(int,java.awt.Color)"""
        val = _OutlineWobbleEffect(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @override
    @overload
    def getStroke(self) -> 'Stroke':
        """public java.awt.Stroke com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getStroke()"""
        return 'Stroke'._wrap(super(OutlineEffect, self).getStroke())

    @override
    @overload
    def getColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getColor()"""
        return 'Color'._wrap(super(OutlineEffect, self).getColor())

    @override
    @overload
    def getJoin(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getJoin()"""
        return int._wrap(super(OutlineEffect, self).getJoin())

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.setValues(java.util.List)"""
        super(_OutlineWobbleEffect, self).setValues(arg0)

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.getValues()"""
        return 'List'._wrap(super(OutlineWobbleEffect, self).getValues())

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
    def setJoin(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setJoin(int)"""
        super(_OutlineEffect, self).setJoin(_int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect()"""
        val = _OutlineWobbleEffect()
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
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.getWidth()"""
        return float._wrap(super(OutlineEffect, self).getWidth())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_OutlineEffect, self).draw(arg0, arg1, arg2, arg3)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStroke(self, arg0: 'Stroke'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setStroke(java.awt.Stroke)"""
        super(_OutlineEffect, self).setStroke(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineEffect.setColor(java.awt.Color)"""
        super(_OutlineEffect, self).setColor(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect()"""
        val = _OutlineWobbleEffect()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.OutlineWobbleEffect.toString()"""
        return str._wrap(super(OutlineWobbleEffect, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect as _FilterEffect
_FilterEffect = _FilterEffect
import java.lang.String as _String
_String = _String
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.awt.Graphics2D as Graphics2D
import java.awt.image.BufferedImageOp as _BufferedImageOp
_BufferedImageOp = _BufferedImageOp
import java.lang.Integer as _int
import java.awt.image.BufferedImageOp as BufferedImageOp
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FilterEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect"""
 
    @staticmethod
    def _wrap(java_value: _FilterEffect) -> 'FilterEffect':
        return FilterEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FilterEffect):
        """
        Dynamic initializer for FilterEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FilterEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FilterEffect__wrapper":
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
    def setFilter(self, arg0: 'BufferedImageOp'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect.setFilter(java.awt.image.BufferedImageOp)"""
        super(_FilterEffect, self).setFilter(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect()"""
        val = _FilterEffect()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'BufferedImageOp'):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect(java.awt.image.BufferedImageOp)"""
        val = _FilterEffect(arg0)
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

    @overload
    def getFilter(self) -> 'BufferedImageOp':
        """public java.awt.image.BufferedImageOp com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect.getFilter()"""
        return 'BufferedImageOp'._wrap(super(FilterEffect, self).getFilter())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_FilterEffect, self).draw(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.FilterEffect()"""
        val = _FilterEffect()
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
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.lang.Float as _float
import com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect as _GradientEffect
_GradientEffect = _GradientEffect
import java.awt.Graphics2D as Graphics2D
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.awt.Color as Color
import java.awt.Color as _Color
_Color = _Color
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GradientEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect"""
 
    @staticmethod
    def _wrap(java_value: _GradientEffect) -> 'GradientEffect':
        return GradientEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GradientEffect):
        """
        Dynamic initializer for GradientEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GradientEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GradientEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCyclic(self, arg0: bool):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setCyclic(boolean)"""
        super(_GradientEffect, self).setCyclic(_boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.toString()"""
        return str._wrap(super(GradientEffect, self).toString())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_GradientEffect, self).draw(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect()"""
        val = _GradientEffect()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getTopColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getTopColor()"""
        return 'Color'._wrap(super(GradientEffect, self).getTopColor())

    @overload
    def setTopColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setTopColor(java.awt.Color)"""
        super(_GradientEffect, self).setTopColor(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getValues()"""
        return 'List'._wrap(super(GradientEffect, self).getValues())

    @overload
    def getOffset(self) -> int:
        """public int com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getOffset()"""
        return int._wrap(super(GradientEffect, self).getOffset())

    @overload
    def getBottomColor(self) -> 'Color':
        """public java.awt.Color com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getBottomColor()"""
        return 'Color'._wrap(super(GradientEffect, self).getBottomColor())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect()"""
        val = _GradientEffect()
        self.__wrapper = val

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setValues(java.util.List)"""
        super(_GradientEffect, self).setValues(arg0)

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setScale(float)"""
        super(_GradientEffect, self).setScale(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Color', arg1: 'Color', arg2: float):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect(java.awt.Color,java.awt.Color,float)"""
        val = _GradientEffect(arg0, arg1, _float.valueOf(arg2))
        self.__wrapper = val

    @overload
    def getScale(self) -> float:
        """public float com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.getScale()"""
        return float._wrap(super(GradientEffect, self).getScale())

    @overload
    def setBottomColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setBottomColor(java.awt.Color)"""
        super(_GradientEffect, self).setBottomColor(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isCyclic(self) -> bool:
        """public boolean com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.isCyclic()"""
        return bool._wrap(super(GradientEffect, self).isCyclic())

    @overload
    def setOffset(self, arg0: int):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.GradientEffect.setOffset(int)"""
        super(_GradientEffect, self).setOffset(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect as _DistanceFieldEffect
_DistanceFieldEffect = _DistanceFieldEffect
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

import java.awt.Graphics2D as Graphics2D
import java.lang.Integer as _int
import java.awt.image.BufferedImage as BufferedImage
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DistanceFieldEffect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect"""
 
    @staticmethod
    def _wrap(java_value: _DistanceFieldEffect) -> 'DistanceFieldEffect':
        return DistanceFieldEffect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DistanceFieldEffect):
        """
        Dynamic initializer for DistanceFieldEffect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DistanceFieldEffect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DistanceFieldEffect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getValues(self) -> 'List':
        """public java.util.List com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.getValues()"""
        return 'List'._wrap(super(DistanceFieldEffect, self).getValues())

    @override
    @overload
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        super(_DistanceFieldEffect, self).draw(arg0, arg1, arg2, arg3)

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
        """public java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.toString()"""
        return str._wrap(super(DistanceFieldEffect, self).toString())

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect()"""
        val = _DistanceFieldEffect()
        self.__wrapper = val

    @override
    @overload
    def setValues(self, arg0: 'List'):
        """public void com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect.setValues(java.util.List)"""
        super(_DistanceFieldEffect, self).setValues(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.tools.hiero.unicodefont.effects.DistanceFieldEffect()"""
        val = _DistanceFieldEffect()
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
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value
from abc import abstractmethod, ABC
import com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect as _ConfigurableEffect_Value
_Value = _ConfigurableEffect_Value.Value
 
class Value():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect.Value"""
 
    @staticmethod
    def _wrap(java_value: _Value) -> 'Value':
        return Value(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Value):
        """
        Dynamic initializer for Value.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Value__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Value__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getObject(self, ):
        """public abstract java.lang.Object com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.getObject()"""
        pass

    @abstractmethod
    def getString(self, ):
        """public abstract java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.getString()"""
        pass

    @abstractmethod
    def setString(self, arg0: str):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.setString(java.lang.String)"""
        pass

    @abstractmethod
    def getName(self, ):
        """public abstract java.lang.String com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.getName()"""
        pass

    @abstractmethod
    def showDialog(self, ):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.ConfigurableEffect$Value.showDialog()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect
from pyquantum_helper import import_once as _import_once
import java.awt.Graphics2D as Graphics2D
import com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect as _Effect
_Effect = _Effect
import java.awt.image.BufferedImage as BufferedImage
from abc import abstractmethod, ABC
try:
    from pygdx.tools.hiero import unicodefont
except ImportError:
    unicodefont = _import_once("pygdx.tools.hiero.unicodefont")

 
class Effect():
    """com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect"""
 
    @staticmethod
    def _wrap(java_value: _Effect) -> 'Effect':
        return Effect(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Effect):
        """
        Dynamic initializer for Effect.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Effect__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Effect__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def draw(self, arg0: 'BufferedImage', arg1: 'Graphics2D', arg2: 'UnicodeFont', arg3: 'Glyph'):
        """public abstract void com.badlogic.gdx.tools.hiero.unicodefont.effects.Effect.draw(java.awt.image.BufferedImage,java.awt.Graphics2D,com.badlogic.gdx.tools.hiero.unicodefont.UnicodeFont,com.badlogic.gdx.tools.hiero.unicodefont.Glyph)"""
        pass