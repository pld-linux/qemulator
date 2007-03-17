%define		_realname   Qemulator
Summary:	GTK2 GUI for qemu
Summary(pl.UTF-8):	GUI w GTK dla qemu
Name:		qemulator
Version:	0.4.5
Release:	0.10
License:	GPL v2
Group:		X11/Applications
Source0:	http://qemulator.createweb.de/plugins/downloads/dodownload.php?file=%{_realname}-%{version}.tar.gz
# Source0-md5:	a9ea901b8e1a9c5d5087220bd8b4f3ed
Patch0:		qemulator-pldpaths.patch
URL:		http://qemulator.createweb.de/
Requires:	libglade2 >= 1:2.5.0
Requires:	python-pygtk-glade >= 2:2.8.0
Requires:	python-pygtk-gtk >= 2:2.8.0
Requires:	python-pycairo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qemulator is a full featured emulation suite for the qemu virtual
engine, with on demand job control written in Python GTK+/Glade2.
Qemulator provides an easy and fast to use image and device
management, a "My machines" list and interactive job control.

It comes with a list of all running jobs from where you can open the
contol panel for each job and perform on demand action. Full
interaction for mounted volumes, usb devices, keyboard and mouse
interaction, screenshots, wave capture and save/restore machine state
and open vnc viewer is provided.

Main Features:
    - Qemulator provides a list view of all qemu-images in your selected
      default images folder.
    - All images on your harddisk can be addet to my machines list, the
      "bookmarks" of Qemulator under a given name and with an icon, even if
      they are not in the default folder or not configured yet.
    - It's possible to store all emulation settings for each image. These
      settings will be loaded each time you select these image for usage.
    - Extra command line for custom qemu options. These extra options will
      also be stored with your settings for the image.

%description -l pl.UTF-8
Qemulator to pełnowartościowy pakiet emulacyjny dla wirtualnego
silnika qemu, z kontrolą zadań na żądanie. Został napisany w Pythonie
przy użyciu GTK+/Glade2. Qemulator zapewnia łatwe i szybkie w użyciu
zarządzanie urządzeniami, listę "Moich maszyn" oraz interaktywną
kontrolę zadań.

Dostarczony jest wraz z listą wszystkich uruchomionych zadań skąd
można uruchomić panel kontrolny dla każdego zadania i przeprowadzić
akcje na żądanie. Zapewnione są: pełna interakcja dla zamontowanych
wolumenów, urządzeń USB, interakcja z myszką i klawiaturą, zrzuty
ekranu, przechwytywanie dźwięku i zachowanie/odtwarzanie stanu maszyn
i otwieranie klienta VNC.

Główne Cechy:
 - Qemulator dostarcza listę wszystkich obrazów qemu w katalogu
   domyślnym obrazów.
 - Wszystkie obrazy na dysku twardym mogą być dodane do listy maszyn,
   zakładek pod zadaną nazwą i ikoną, nawet gdy nie są w domyślnym
   katalogu albo nie są jeszcze skonfigurowane.
 - Jest możliwe przechowywanie wszystkich ustawień emulacji dla
   każdego obrazu. Te ustawienia będą załadowane za każdym razem po
   wybraniu danego obrazu do użytku.
 - Dodatkowe komendy linii poleceń dla własnych opcji qemu. Te
   dodatkowe opcję będą również przechowywane wraz z ustawieniami dla
   danego obrazu.

%prep
%setup -q -n %{_realname}-%{version}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_libdir}/%{name},%{_bindir},%{_desktopdir},%{_pixmapsdir}}

find -type f -exec sed -i -e 's|#!.*python.*|#!%{_bindir}/python|g' "{}" ";"
cp usr/local/share/%{name}/icons/README usr/local/share/%{name}/icons/README-icons
cp usr/local/share/pixmaps/%{name}/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp usr/local/share/applications/* $RPM_BUILD_ROOT%{_desktopdir}
mv usr/local/lib/%{name}/%{name}.glade $RPM_BUILD_ROOT%{_datadir}/%{name}
cp usr/local/lib/%{name}/* $RPM_BUILD_ROOT%{_libdir}/%{name}
cp --no-dereference usr/local/bin/* $RPM_BUILD_ROOT%{_bindir}
cp -r usr/local/share/{locale,icons} $RPM_BUILD_ROOT%{_datadir}
cp -r usr/local/share/pixmaps/*.svg $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{_realname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc README usr/local/share/%{name}/icons/README-icons
%{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.py
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/*/%{name}.png
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_pixmapsdir}/*.svg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
