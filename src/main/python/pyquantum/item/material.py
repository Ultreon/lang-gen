from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.item.material.ItemMaterial as _ItemMaterial_Builder
_Builder = _ItemMaterial_Builder.Builder
import dev.ultreon.quantum.item.material.ItemMaterial as _ItemMaterial
_ItemMaterial = _ItemMaterial
from abc import abstractmethod, ABC
 
class ItemMaterial():
    """dev.ultreon.quantum.item.material.ItemMaterial"""
 
    @staticmethod
    def _wrap(java_value: _ItemMaterial) -> 'ItemMaterial':
        return ItemMaterial(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemMaterial):
        """
        Dynamic initializer for ItemMaterial.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemMaterial__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemMaterial__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getEfficiency(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getEfficiency()"""
        pass

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial.builder()"""
        return Builder._wrap(_ItemMaterial.builder())

    @abstractmethod
    def getAttackDamage(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getAttackDamage()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterial
import dev.ultreon.quantum.item.material.ItemMaterial as _ItemMaterial_Builder
_Builder = _ItemMaterial_Builder.Builder
import dev.ultreon.quantum.item.material.ItemMaterial as _ItemMaterial
_ItemMaterial = _ItemMaterial
from abc import abstractmethod, ABC
 
class ItemMaterial():
    """dev.ultreon.quantum.item.material.ItemMaterial"""
 
    @staticmethod
    def _wrap(java_value: _ItemMaterial) -> 'ItemMaterial':
        return ItemMaterial(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemMaterial):
        """
        Dynamic initializer for ItemMaterial.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemMaterial__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemMaterial__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getEfficiency(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getEfficiency()"""
        pass

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial.builder()"""
        return Builder._wrap(_ItemMaterial.builder())

    @abstractmethod
    def getAttackDamage(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getAttackDamage()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterial 
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterials
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.item.material.ItemMaterials as _ItemMaterials
_ItemMaterials = _ItemMaterials
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ItemMaterials():
    """dev.ultreon.quantum.item.material.ItemMaterials"""
 
    @staticmethod
    def _wrap(java_value: _ItemMaterials) -> 'ItemMaterials':
        return ItemMaterials(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ItemMaterials):
        """
        Dynamic initializer for ItemMaterials.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ItemMaterials__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ItemMaterials__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    # public static final dev.ultreon.quantum.item.material.ItemMaterial dev.ultreon.quantum.item.material.ItemMaterials.STONE
    STONE: 'ItemMaterial' = _wrap(_ItemMaterial.STONE)

    # public static final dev.ultreon.quantum.item.material.ItemMaterial dev.ultreon.quantum.item.material.ItemMaterials.WOOD
    WOOD: 'ItemMaterial' = _wrap(_ItemMaterial.WOOD)


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
        """public dev.ultreon.quantum.item.material.ItemMaterials()"""
        val = _ItemMaterials()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.material.ItemMaterials()"""
        val = _ItemMaterials()
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
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterial$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.item.material.ItemMaterial as _ItemMaterial_Builder
_Builder = _ItemMaterial_Builder.Builder
import dev.ultreon.quantum.item.material.ItemMaterial as _ItemMaterial
_ItemMaterial = _ItemMaterial
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """dev.ultreon.quantum.item.material.ItemMaterial.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def build(self) -> 'ItemMaterial':
        """public dev.ultreon.quantum.item.material.ItemMaterial dev.ultreon.quantum.item.material.ItemMaterial$Builder.build()"""
        return 'ItemMaterial'._wrap(super(Builder, self).build())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def attackDamage(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial$Builder.attackDamage(float)"""
        return 'Builder'._wrap(super(_Builder, self).attackDamage(_float.valueOf(arg0)))

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
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder()"""
        val = _Builder()
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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def efficiency(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial$Builder.efficiency(float)"""
        return 'Builder'._wrap(super(_Builder, self).efficiency(_float.valueOf(arg0)))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder()"""
        val = _Builder()
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