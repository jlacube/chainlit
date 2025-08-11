/**
 * TypeScript interfaces for Composer Button functionality
 */

export interface IComposerButton {
  id: string;
  label: string;
  style: 'primary' | 'secondary' | 'outline';
  data?: Record<string, any>;
}

export interface ComposerButtonData {
  id: string;
  label: string;
  callback: string;
  icon?: string;
  style?: 'primary' | 'secondary' | 'ghost';
  disabled?: boolean;
  tooltip?: string;
}

export interface SetComposerButtonsMessage {
  type: 'set_composer_buttons';
  buttons: ComposerButtonData[];
}

export interface UpdateComposerButtonMessage {
  type: 'update_composer_button';
  buttonId: string;
  updates: Partial<ComposerButtonData>;
}

export interface RemoveComposerButtonsMessage {
  type: 'remove_composer_buttons';
}

export interface ComposerButtonClickEvent {
  type: 'composer_button_click';
  buttonId: string;
  callback: string;
}

export interface ComposerButtonErrorMessage {
  type: 'composer_button_error';
  buttonId: string;
  error: string;
}
