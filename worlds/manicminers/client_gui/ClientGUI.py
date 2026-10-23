from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..Client import ManicMinersContext

from .ClientGUILayout import OverviewTabLayout, LevelsTabLayout, TimesTabLayout, CrystalsTabLayout, InventoryTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class ManicMinersManager(gui):
        ctx: ManicMinersContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Manic Miners Client"

        overview_tab_layout: OverviewTabLayout
        overview_tab: Widget
        
        levels_tab_layout: LevelsTabLayout
        levels_tab: Widget
        
        times_tab_layout: TimesTabLayout
        times_tab: Widget
        
        crystals_tab_layout: CrystalsTabLayout
        crystals_tab: Widget
        
        inventory_tab_layout: InventoryTabLayout
        inventory_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.overview_tab_layout = OverviewTabLayout(self.ctx)
            self.overview_tab = self.add_client_tab("Chief: Overview", self.overview_tab_layout)
            self.levels_tab_layout = LevelsTabLayout(self.ctx)
            self.levels_tab = self.add_client_tab("Bandit: Levels", self.levels_tab_layout)
            self.times_tab_layout = TimesTabLayout(self.ctx)
            self.times_tab = self.add_client_tab("Jet: Times", self.times_tab_layout)
            self.crystals_tab_layout = CrystalsTabLayout(self.ctx)
            self.crystals_tab = self.add_client_tab("Sparks: Crystals", self.crystals_tab_layout)
            self.inventory_tab_layout = InventoryTabLayout(self.ctx)
            self.inventory_tab = self.add_client_tab("Axle: Inventory", self.inventory_tab_layout)
            
            return container

        def update_tabs(self) -> None:
            self.overview_tab_layout.update()
            self.levels_tab_layout.update()
            self.times_tab_layout.update()
            self.crystals_tab_layout.update()
            self.inventory_tab_layout.update()
            
        def clear_tabs(self) -> None:
            self.overview_tab_layout.clear_widgets()
            self.levels_tab_layout.clear_widgets()
            self.times_tab_layout.clear_widgets()
            self.crystals_tab_layout.clear_widgets()
            self.inventory_tab_layout.clear_widgets()

    return ManicMinersManager