from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.recipe.RecipeType as _RecipeType
_RecipeType = _RecipeType
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.recipe.Recipe as _Recipe
_Recipe = _Recipe
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.recipe.RecipeType as _RecipeType_RecipeDeserializer
_RecipeDeserializer = _RecipeType_RecipeDeserializer.RecipeDeserializer
import java.lang.Integer as _int
import de.marhali.json5.Json5Object as Json5Object
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RecipeType():
    """dev.ultreon.quantum.recipe.RecipeType"""
 
    @staticmethod
    def _wrap(java_value: _RecipeType) -> 'RecipeType':
        return RecipeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecipeType):
        """
        Dynamic initializer for RecipeType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecipeType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecipeType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def deserialize(self, arg0: 'Identifier', arg1: 'Json5Object') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeType.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        return 'Recipe'._wrap(super(_RecipeType, self).deserialize(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getKey(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeType.getKey()"""
        return 'util.Identifier'._wrap(super(RecipeType, self).getKey())

    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.getId()"""
        return int._wrap(super(RecipeType, self).getId())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.recipe.RecipeType.toString()"""
        return str._wrap(super(RecipeType, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.hashCode()"""
        return int._wrap(super(RecipeType, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.recipe.RecipeType.equals(java.lang.Object)"""
        return bool._wrap(super(_RecipeType, self).equals(arg0))

    @overload
    def deserializer(self) -> 'RecipeDeserializer':
        """public dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T> dev.ultreon.quantum.recipe.RecipeType.deserializer()"""
        return 'RecipeDeserializer'._wrap(super(RecipeType, self).deserializer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'RecipeDeserializer'):
        """public dev.ultreon.quantum.recipe.RecipeType(dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T>)"""
        val = _RecipeType(arg0)
        self.__wrapper = val


RecipeType.CRAFTING = RecipeType._wrap(_CRAFTING.CRAFTING)

 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeType
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.recipe.RecipeType as _RecipeType
_RecipeType = _RecipeType
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.recipe.Recipe as _Recipe
_Recipe = _Recipe
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.recipe.RecipeType as _RecipeType_RecipeDeserializer
_RecipeDeserializer = _RecipeType_RecipeDeserializer.RecipeDeserializer
import java.lang.Integer as _int
import de.marhali.json5.Json5Object as Json5Object
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RecipeType():
    """dev.ultreon.quantum.recipe.RecipeType"""
 
    @staticmethod
    def _wrap(java_value: _RecipeType) -> 'RecipeType':
        return RecipeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecipeType):
        """
        Dynamic initializer for RecipeType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecipeType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecipeType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def deserialize(self, arg0: 'Identifier', arg1: 'Json5Object') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeType.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        return 'Recipe'._wrap(super(_RecipeType, self).deserialize(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getKey(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeType.getKey()"""
        return 'util.Identifier'._wrap(super(RecipeType, self).getKey())

    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.getId()"""
        return int._wrap(super(RecipeType, self).getId())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.recipe.RecipeType.toString()"""
        return str._wrap(super(RecipeType, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.hashCode()"""
        return int._wrap(super(RecipeType, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.recipe.RecipeType.equals(java.lang.Object)"""
        return bool._wrap(super(_RecipeType, self).equals(arg0))

    @overload
    def deserializer(self) -> 'RecipeDeserializer':
        """public dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T> dev.ultreon.quantum.recipe.RecipeType.deserializer()"""
        return 'RecipeDeserializer'._wrap(super(RecipeType, self).deserializer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'RecipeDeserializer'):
        """public dev.ultreon.quantum.recipe.RecipeType(dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T>)"""
        val = _RecipeType(arg0)
        self.__wrapper = val


RecipeType.CRAFTING = RecipeType._wrap(_CRAFTING.CRAFTING)

 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeType 
 
 
# CLASS: dev.ultreon.quantum.recipe.Recipes
import dev.ultreon.quantum.recipe.Recipes as _Recipes
_Recipes = _Recipes
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
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Recipes():
    """dev.ultreon.quantum.recipe.Recipes"""
 
    @staticmethod
    def _wrap(java_value: _Recipes) -> 'Recipes':
        return Recipes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Recipes):
        """
        Dynamic initializer for Recipes.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Recipes__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Recipes__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.recipe.Recipes()"""
        val = _Recipes()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.recipe.Recipes.init()"""
            _Recipes.init()

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

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.recipe.Recipes()"""
        val = _Recipes()
        self.__wrapper = val

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
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeRegistry
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.recipe.Recipe as _Recipe
_Recipe = _Recipe
import java.util.Set as _Set
_Set = _Set
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Set as Set
import dev.ultreon.quantum.registry.AbstractRegistry as _AbstractRegistry
_AbstractRegistry = _AbstractRegistry
import dev.ultreon.quantum.recipe.RecipeRegistry as _RecipeRegistry
_RecipeRegistry = _RecipeRegistry
import java.lang.Integer as _int
import dev.ultreon.quantum.util.PagedList as _PagedList
_PagedList = _PagedList
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

from builtins import int
 
class RecipeRegistry():
    """dev.ultreon.quantum.recipe.RecipeRegistry"""
 
    @staticmethod
    def _wrap(java_value: _RecipeRegistry) -> 'RecipeRegistry':
        return RecipeRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecipeRegistry):
        """
        Dynamic initializer for RecipeRegistry.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecipeRegistry__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecipeRegistry__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<dev.ultreon.quantum.util.Identifier, T>> dev.ultreon.quantum.recipe.RecipeRegistry.entries() throws java.lang.IllegalAccessException"""
        return 'Set'._wrap(super(RecipeRegistry, self).entries())

    @override
    @overload
    def random(self) -> object:
        """public V dev.ultreon.quantum.registry.AbstractRegistry.random()"""
        return object._wrap(super(registry.AbstractRegistry, self).random())

    @overload
    def __init__(self, *arg0: 'Recipe'):
        """public dev.ultreon.quantum.recipe.RecipeRegistry(T...)"""
        val = _RecipeRegistry(arg0)
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def keys(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.recipe.RecipeRegistry.keys()"""
        return 'List'._wrap(super(RecipeRegistry, self).keys())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getRecipes(self, arg0: int, arg1: 'Inventory') -> 'util.PagedList':
        """public dev.ultreon.quantum.util.PagedList<T> dev.ultreon.quantum.recipe.RecipeRegistry.getRecipes(int,dev.ultreon.quantum.menu.Inventory)"""
        return 'util.PagedList'._wrap(super(_RecipeRegistry, self).getRecipes(_int.valueOf(arg0), arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def values(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.recipe.RecipeRegistry.values()"""
        return 'List'._wrap(super(RecipeRegistry, self).values())

    @overload
    def getKey(self, arg0: 'Recipe') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeRegistry.getKey(T)"""
        return 'util.Identifier'._wrap(super(_RecipeRegistry, self).getKey(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def freeze(self):
        """public void dev.ultreon.quantum.recipe.RecipeRegistry.freeze()"""
        super(RecipeRegistry, self).freeze()

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
    def register(self, arg0: 'Identifier', arg1: 'Recipe'):
        """public void dev.ultreon.quantum.recipe.RecipeRegistry.register(dev.ultreon.quantum.util.Identifier,T)"""
        super(_RecipeRegistry, self).register(arg0, arg1)

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.quantum.recipe.RecipeRegistry.getType()"""
        return 'type.Class'._wrap(super(RecipeRegistry, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'Identifier') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeRegistry.get(dev.ultreon.quantum.util.Identifier)"""
        return 'Recipe'._wrap(super(_RecipeRegistry, self).get(arg0))

    @overload
    def removeRecipe(self, arg0: 'Identifier') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeRegistry.removeRecipe(dev.ultreon.quantum.util.Identifier)"""
        return 'Recipe'._wrap(super(_RecipeRegistry, self).removeRecipe(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.recipe.CraftingRecipe
from pyquantum_helper import import_once as _import_once
from builtins import str
import dev.ultreon.quantum.item.ItemStack as _ItemStack
_ItemStack = _ItemStack
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.recipe.RecipeType as _RecipeType
_RecipeType = _RecipeType
import dev.ultreon.quantum.recipe.CraftingRecipe as _CraftingRecipe
_CraftingRecipe = _CraftingRecipe
try:
    from pyquantum import item
except ImportError:
    item = _import_once("pyquantum.item")

import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import dev.ultreon.quantum.recipe.Recipe as _Recipe
_Recipe = _Recipe
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.lang.Integer as _int
import de.marhali.json5.Json5Object as Json5Object
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

import java.lang.Class as _Class
_Class = _Class
 
class CraftingRecipe():
    """dev.ultreon.quantum.recipe.CraftingRecipe"""
 
    @staticmethod
    def _wrap(java_value: _CraftingRecipe) -> 'CraftingRecipe':
        return CraftingRecipe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CraftingRecipe):
        """
        Dynamic initializer for CraftingRecipe.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CraftingRecipe__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CraftingRecipe__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: 'List', arg1: 'ItemStack'):
        """public dev.ultreon.quantum.recipe.CraftingRecipe(java.util.List<dev.ultreon.quantum.item.ItemStack>,dev.ultreon.quantum.item.ItemStack)"""
        val = _CraftingRecipe(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.recipe.CraftingRecipe.toString()"""
        return str._wrap(super(CraftingRecipe, self).toString())

    @override
    @overload
    def getType(self) -> 'RecipeType':
        """public dev.ultreon.quantum.recipe.RecipeType<dev.ultreon.quantum.recipe.CraftingRecipe> dev.ultreon.quantum.recipe.CraftingRecipe.getType()"""
        return 'RecipeType'._wrap(super(CraftingRecipe, self).getType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def canCraft(self, arg0: 'Inventory') -> bool:
        """public boolean dev.ultreon.quantum.recipe.CraftingRecipe.canCraft(dev.ultreon.quantum.menu.Inventory)"""
        return bool._wrap(super(_CraftingRecipe, self).canCraft(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def craft(self, arg0: 'Inventory') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.CraftingRecipe.craft(dev.ultreon.quantum.menu.Inventory)"""
        return 'item.ItemStack'._wrap(super(_CraftingRecipe, self).craft(arg0))

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
    def getId(self) -> 'util.Identifier':
        """public default dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.Recipe.getId()"""
        return 'util.Identifier'._wrap(super(Recipe, self).getId())

    @staticmethod
    @overload
    def deserialize(arg0: 'Identifier', arg1: 'Json5Object') -> 'CraftingRecipe':
        """public static dev.ultreon.quantum.recipe.CraftingRecipe dev.ultreon.quantum.recipe.CraftingRecipe.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        return CraftingRecipe._wrap(_CraftingRecipe.deserialize(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def ingredients(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.recipe.CraftingRecipe.ingredients()"""
        return 'List'._wrap(super(CraftingRecipe, self).ingredients())

    @override
    @overload
    def result(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.CraftingRecipe.result()"""
        return 'item.ItemStack'._wrap(super(CraftingRecipe, self).result())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.recipe.CraftingRecipe.hashCode()"""
        return int._wrap(super(CraftingRecipe, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.recipe.CraftingRecipe.equals(java.lang.Object)"""
        return bool._wrap(super(_CraftingRecipe, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeManager
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import server
except ImportError:
    server = _import_once("pyquantum.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.recipe.Recipe as _Recipe
_Recipe = _Recipe
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import dev.ultreon.quantum.util.PagedList as _PagedList
_PagedList = _PagedList
import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
try:
    from pyquantum import resources
except ImportError:
    resources = _import_once("pyquantum.resources")

import dev.ultreon.quantum.server.QuantumServer as _QuantumServer
_QuantumServer = _QuantumServer
from builtins import bool
import java.lang.Long as _long
import dev.ultreon.quantum.recipe.RecipeManager as _RecipeManager
_RecipeManager = _RecipeManager
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RecipeManager():
    """dev.ultreon.quantum.recipe.RecipeManager"""
 
    @staticmethod
    def _wrap(java_value: _RecipeManager) -> 'RecipeManager':
        return RecipeManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecipeManager):
        """
        Dynamic initializer for RecipeManager.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecipeManager__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecipeManager__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def freeze(self):
        """public void dev.ultreon.quantum.recipe.RecipeManager.freeze()"""
        super(RecipeManager, self).freeze()

    @overload
    def load(self, arg0: 'ResourceManager'):
        """public void dev.ultreon.quantum.recipe.RecipeManager.load(dev.ultreon.quantum.resources.ResourceManager)"""
        super(_RecipeManager, self).load(arg0)

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
    def unload(self):
        """public void dev.ultreon.quantum.recipe.RecipeManager.unload()"""
        super(RecipeManager, self).unload()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def fireRecipeModifications(self):
        """public void dev.ultreon.quantum.recipe.RecipeManager.fireRecipeModifications()"""
        super(RecipeManager, self).fireRecipeModifications()

    @overload
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.recipe.RecipeManager(dev.ultreon.quantum.server.QuantumServer)"""
        val = _RecipeManager(arg0)
        self.__wrapper = val

    @overload
    def register(self, arg0: 'Identifier', arg1: 'Recipe'):
        """public <T extends dev.ultreon.quantum.recipe.Recipe> void dev.ultreon.quantum.recipe.RecipeManager.register(dev.ultreon.quantum.util.Identifier,T)"""
        super(_RecipeManager, self).register(arg0, arg1)

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

    @staticmethod
    @overload
    def get() -> 'RecipeManager':
        """public static dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.recipe.RecipeManager.get()"""
        return RecipeManager._wrap(_RecipeManager.get())

    @overload
    def getRecipes(self, arg0: 'RecipeType', arg1: int, arg2: 'Inventory') -> 'util.PagedList':
        """public <T extends dev.ultreon.quantum.recipe.Recipe> dev.ultreon.quantum.util.PagedList<? extends T> dev.ultreon.quantum.recipe.RecipeManager.getRecipes(dev.ultreon.quantum.recipe.RecipeType<T>,int,dev.ultreon.quantum.menu.Inventory)"""
        return 'util.PagedList'._wrap(super(_RecipeManager, self).getRecipes(arg0, _int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def get(self, arg0: 'Identifier', arg1: 'RecipeType') -> 'Recipe':
        """public <T extends dev.ultreon.quantum.recipe.Recipe> T dev.ultreon.quantum.recipe.RecipeManager.get(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.recipe.RecipeType<T>)"""
        return 'Recipe'._wrap(super(_RecipeManager, self).get(arg0, arg1))

    @overload
    def getRecipes(self, arg0: 'RecipeType') -> 'Collection':
        """public <T extends dev.ultreon.quantum.recipe.Recipe> java.util.Collection<T> dev.ultreon.quantum.recipe.RecipeManager.getRecipes(dev.ultreon.quantum.recipe.RecipeType<T>)"""
        return 'Collection'._wrap(super(_RecipeManager, self).getRecipes(arg0))

    @overload
    def getKey(self, arg0: 'RecipeType', arg1: 'Recipe') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeManager.getKey(dev.ultreon.quantum.recipe.RecipeType<?>,dev.ultreon.quantum.recipe.Recipe)"""
        return 'util.Identifier'._wrap(super(_RecipeManager, self).getKey(arg0, arg1))

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.recipe.RecipeManager.getServer()"""
        return 'server.QuantumServer'._wrap(super(RecipeManager, self).getServer())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.recipe.RecipeType as _RecipeType_RecipeDeserializer
_RecipeDeserializer = _RecipeType_RecipeDeserializer.RecipeDeserializer
import de.marhali.json5.Json5Object as Json5Object
from abc import abstractmethod, ABC
 
class RecipeDeserializer():
    """dev.ultreon.quantum.recipe.RecipeType.RecipeDeserializer"""
 
    @staticmethod
    def _wrap(java_value: _RecipeDeserializer) -> 'RecipeDeserializer':
        return RecipeDeserializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecipeDeserializer):
        """
        Dynamic initializer for RecipeDeserializer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecipeDeserializer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecipeDeserializer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def deserialize(self, arg0: 'Identifier', arg1: 'Json5Object'):
        """public abstract T dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.recipe.Recipe
from pyquantum_helper import import_once as _import_once
try:
    from pyquantum import util
except ImportError:
    util = _import_once("pyquantum.util")

import dev.ultreon.quantum.util.Identifier as _Identifier
_Identifier = _Identifier
from abc import abstractmethod, ABC
import dev.ultreon.quantum.recipe.Recipe as _Recipe
_Recipe = _Recipe
try:
    from pyquantum import menu
except ImportError:
    menu = _import_once("pyquantum.menu")

 
class Recipe():
    """dev.ultreon.quantum.recipe.Recipe"""
 
    @staticmethod
    def _wrap(java_value: _Recipe) -> 'Recipe':
        return Recipe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Recipe):
        """
        Dynamic initializer for Recipe.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Recipe__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Recipe__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getId(self) -> 'util.Identifier':
        """public default dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.Recipe.getId()"""
        return 'util.Identifier'._wrap(super(Recipe, self).getId())

    @abstractmethod
    def craft(self, arg0: 'Inventory'):
        """public abstract dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.Recipe.craft(dev.ultreon.quantum.menu.Inventory)"""
        pass

    @abstractmethod
    def result(self, ):
        """public abstract dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.Recipe.result()"""
        pass

    @abstractmethod
    def canCraft(self, arg0: 'Inventory'):
        """public abstract boolean dev.ultreon.quantum.recipe.Recipe.canCraft(dev.ultreon.quantum.menu.Inventory)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract dev.ultreon.quantum.recipe.RecipeType<?> dev.ultreon.quantum.recipe.Recipe.getType()"""
        pass

    @abstractmethod
    def ingredients(self, ):
        """public abstract java.util.List<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.recipe.Recipe.ingredients()"""
        pass