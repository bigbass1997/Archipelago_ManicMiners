from typing import List, Optional, Tuple

from kvui import GameManager

from kivy.uix.layout import Layout
from kivy.uix.widget import Widget

from ..Client import ManicMinersContext

from .ClientGUILayout import ChiefsReportTabLayout, DocsMapTabLayout, JetsStopwatchTabLayout, SparksReactorsTabLayout, AxlesHangarTabLayout


def bootstrap_client_gui(gui: Optional[type[GameManager]]) -> type[GameManager]:
    class ManicMinersManager(gui):
        ctx: ManicMinersContext

        logging_pairs: List[Tuple[str, str]] = [("Client", "Archipelago")]
        base_title: str = "Archipelago Manic Miners Client"

        chiefsreport_tab_layout: ChiefsReportTabLayout
        chiefsreport_tab: Widget
        
        docsmap_tab_layout: DocsMapTabLayout
        docsmap_tab: Widget
        
        jetsstopwatch_tab_layout: JetsStopwatchTabLayout
        jetsstopwatch_tab: Widget
        
        sparksreactors_tab_layout: SparksReactorsTabLayout
        sparksreactors_tab: Widget
        
        axleshangar_tab_layout: AxlesHangarTabLayout
        axleshangar_tab: Widget

        def build(self) -> Layout:
            container: Layout = super().build()

            self.chiefsreport_tab_layout = ChiefsReportTabLayout(self.ctx)
            self.chiefsreport_tab = self.add_client_tab("Chief's Report", self.chiefsreport_tab_layout)
            self.docsmap_tab_layout = DocsMapTabLayout(self.ctx)
            self.docsmap_tab = self.add_client_tab("Doc's Map", self.docsmap_tab_layout)
            self.jetsstopwatch_tab_layout = JetsStopwatchTabLayout(self.ctx)
            self.jetsstopwatch_tab = self.add_client_tab("Jet's Stopwatch", self.jetsstopwatch_tab_layout)
            self.sparksreactors_tab_layout = SparksReactorsTabLayout(self.ctx)
            self.sparksreactors_tab = self.add_client_tab("Sparks' Reactors", self.sparksreactors_tab_layout)
            self.axleshangar_tab_layout = AxlesHangarTabLayout(self.ctx)
            self.axleshangar_tab = self.add_client_tab("Axle's Hangar", self.axleshangar_tab_layout)
            
            return container

        def update_tabs(self) -> None:
            self.chiefsreport_tab_layout.update()
            self.docsmap_tab_layout.update()
            self.jetsstopwatch_tab_layout.update()
            self.sparksreactors_tab_layout.update()
            self.axleshangar_tab_layout.update()
            
        def clear_tabs(self) -> None:
            self.chiefsreport_tab_layout.clear_widgets()
            self.docsmap_tab_layout.clear_widgets()
            self.jetsstopwatch_tab_layout.clear_widgets()
            self.sparksreactors_tab_layout.clear_widgets()
            self.axleshangar_tab_layout.clear_widgets()

    return ManicMinersManager